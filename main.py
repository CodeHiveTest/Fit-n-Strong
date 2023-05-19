from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from sqlalchemy.exc import SQLAlchemyError


from flask import Flask,jsonify,request


from sqlalchemy import create_engine

database_addres = 'mysql+pymysql://fit:Testing_2023@localhost:3306/fitstrong'


engine = create_engine(database_addres, echo = False)

from sqlalchemy import Select

from sqlalchemy.orm import Session

session = Session(engine)

class Base(DeclarativeBase):
    pass



class Rutina(Base):
    __tablename__ = "rutina"
    rutina_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(45), default="NULL")
    grupo_muscular: Mapped[str] = mapped_column(String(45), default="NULL")
    ejercicio: Mapped[List["Ejercicio"]] = relationship(back_populates="rutina")

class Ejercicio(Base):
    __tablename__ = "ejercicio"
    ejercicio_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(45), nullable=False)
    repeticiones: Mapped[int] = mapped_column(nullable=False)
    duracion: Mapped[int] = mapped_column(nullable=False)
    peso: Mapped[int] = mapped_column(nullable=False)
    rutina_id: Mapped[int] = mapped_column(ForeignKey("rutina.rutina_id"), default="NULL")
    rutina: Mapped["Rutina"] = relationship(back_populates="ejercicio")


from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/rutina', methods=['GET'])
def get_rutina():
    id_rutina = request.args.get("id")
    stmt = Select(Rutina).where(Rutina.rutina_id == id_rutina)
    try:
        rutina = session.scalars(stmt).one()
    except SQLAlchemyError as e:
        return _corsify_actual_response(jsonify({"status": 500}))
    return jsonify({"nombre":rutina.nombre, "grupo_muscular": rutina.grupo_muscular})

@app.route('/ejercicio', methods=['GET'])
def get_ejercicio():
    id_ejercicio = request.args.get("id")
    stmt = Select(Ejercicio).where(Ejercicio.ejercicio_id == id_ejercicio)
    try:
        ejercicio = session.scalars(stmt).one()
    except SQLAlchemyError as e:
        return _corsify_actual_response(jsonify({"status": 500}))
    return jsonify({"nombre":ejercicio.nombre,
                    "repeticiones":ejercicio.repeticiones,
                     "duracion": ejercicio.duracion,
                      "peso": ejercicio.peso })


@app.route('/rutinas', methods=['GET'])
def get_rutinas():
    stmt = Select(Rutina)
    d = []
    if session.scalars(stmt) == None:
        response = jsonify({"response": "No hay rutina"})
        response.headers['Access-Control-Allow-Origin'] = '*'
    for i in session.scalars(stmt):
        d.append({"nombre": str(i.nombre), "grupo_muscular": str(i.grupo_muscular), "id": i.rutina_id})

    return _corsify_actual_response(jsonify(d))

@app.route('/ejercicios', methods=['GET'])
def get_ejercicios_by_rutina():
    rut_id = request.args.get("id")
    stmt = Select(Ejercicio).where(Ejercicio.rutina_id == rut_id)
    d = [] 
    if session.scalars(stmt) == None:
        response = jsonify({"response":"No se encontraron ejercicios asociados a esa rutina"})
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    for i in session.scalars(stmt):
        d.append({"ejercicio_id": i.ejercicio_id,
                "nombre": i.nombre,
				"repeticiones": i.repeticiones,
				"duracion": i.duracion,
 				"peso": i.peso})
    response = jsonify(d)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return(response)


@app.route('/rutinas', methods=['POST', 'OPTIONS','DELETE'])
@cross_origin()
def crear_rutina():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    elif request.method == 'DELETE':
        rut_id = request.args.get('id')
        rut = session.get(Rutina,rut_id)
        if rut == None:
            return(jsonify({"status":"No existe la rutina"}))
        try:
            session.delete(rut)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            return _corsify_actual_response(jsonify({"status": 500}))
        return _corsify_actual_response(jsonify({"status": 201}))
        
    elif request.method == 'POST':
        content = request.get_json()
        newRutina = Rutina(nombre = content["nombre"],
        grupo_muscular = content["grupo_muscular"])
        session.add(newRutina)
        try:
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(f"\n {error} \n")
            session.rollback()
            return _corsify_actual_response(jsonify({"status": 500}))
        return _corsify_actual_response(jsonify({"status": 201}))
    else:
       raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))
    
@app.route('/ejercicios', methods=['POST', 'OPTIONS','DELETE'])
@cross_origin()
def crear_ejercicio():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()

    elif request.method == 'DELETE':
        rut_id = request.args.get('id')
        rut = session.get(Ejercicio,rut_id)
        response = jsonify(dict())
        if rut == None:
            return(jsonify({"status":"No existe la rutina"}))
        try:
            session.delete(rut)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            return _corsify_actual_response(jsonify({"status": 500}))
        return _corsify_actual_response(jsonify({"status": 200}))


    elif request.method == 'POST':

        content = request.get_json()
        newEjercicio = Ejercicio(nombre = content["nombre"])
        if "rutina_id" not in content:
            return(jsonify({"Respuesta":"No se añadio la rutina a la que pertence"}))
        newEjercicio.rutina_id = content["rutina_id"]
        if "repeticiones" in content:
            newEjercicio.repeticiones = content["repeticiones"]
        if "duracion" in content:
            newEjercicio.duracion = content["duracion"]
        if "peso" in content:
            newEjercicio.peso = content["peso"]
        session.add(newEjercicio)
        try:
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(f"\n {error} \n")
            session.rollback()
            return _corsify_actual_response(jsonify({"status": 500}))
        return _corsify_actual_response(jsonify({"status": 201}))
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))



@app.route('/rutinas', methods=['PUT'])
def update_rutina():
    content = request.get_json()
    if "rutina_id" not in content:
        return(jsonify({"Respuesta":"No se añadió el id de la rutina"}))
    stmt = Select(Rutina).where(Rutina.rutina_id == content["rutina_id"])
    rutina = session.scalars(stmt).one()
    if "nombre" in content:
        rutina.nombre = content["nombre"]
    if "grupo_muscular" in content:
        rutina.grupo_muscular = content["grupo_muscular"]
    try:
        session.commit()
        return _corsify_actual_response(jsonify({"status": 200}))
    except SQLAlchemyError as e:
        session.rollback()    
        return _corsify_actual_response(jsonify({"status": 500}))

@app.route('/ejercicios', methods=['PUT'])
def update_ejercicio():
    content = request.get_json()
    print(content)
    if "ejercicio_id" not in content:
        return(jsonify({"Respuesta":"No se añadió el id de la rutina"}))
    stmt = Select(Ejercicio).where(Ejercicio.ejercicio_id == content["ejercicio_id"])
    ejercicio = session.scalars(stmt).one()
    if "nombre" in content:
        ejercicio.nombre = content["nombre"]
    if "repeticiones" in content:
        ejercicio.repeticiones = content["repeticiones"]
    if "duracion" in content:
        ejercicio.duracion = content["duracion"]
    if "peso" in content:
        ejercicio.peso = content["peso"]
    try:
        print("\n Se intenta update \n")
        session.commit()
        return _corsify_actual_response(jsonify({"status": 200}))
    except SQLAlchemyError as e:
        session.rollback()    
        return _corsify_actual_response(jsonify({"status": 500}))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080,debug=True)
