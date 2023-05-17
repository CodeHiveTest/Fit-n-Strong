from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

import json
from flask import Flask,jsonify,request

import flask

from sqlalchemy import create_engine

database_addres = 'mysql+pymysql://fit:Testing_2023@localhost:3306/fitstrong'


engine = create_engine(database_addres, echo = False)

from sqlalchemy import Select, insert, delete

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


#stmt = Select(Ejercicio).where(Ejercicio.ejercicio_id == 1)
#session.execute(stmt).all()
#for i in session.scalars(stmt):
#    print(i.nombre)

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
   # response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/rutinas', methods=['OPTIONS'])
def reply_headers():
    a = jsonify({"a":"1"})
    a.headers['Access-Control-Allow-Headers'] = "content-type"
    a.headers['Access-Control-Allow-Origin'] = '*'
   # a.headers['Content-Type'] = "text/plain"
    a.headers['Access-Control-Allow-Methods'] = "PUT, GET, POST, DELETE, OPTIONS"
    return a

@app.route('/rutinas', methods=['GET'])
def get_rutinas():
    #content = request.json()
    stmt = Select(Rutina)
    d = []
    if session.scalar(stmt) == None:
        response = jsonify({"response": "No hay rutina"})
        response.headers['Access-Control-Allow-Origin'] = '*'
    for i in session.scalars(stmt):
        d.append({"nombre": str(i.nombre), "grupo_muscular": str(i.grupo_muscular), "id": i.rutina_id})

    return _corsify_actual_response(jsonify(d))

@app.route('/ejercicios', methods=['GET'])
def get_ejercicios_by_rutina():
    rut_id = request.args.get("rut_id")
    stmt = Select(Ejercicio).where(Ejercicio.rutina_id == rut_id)
    d = dict()
    if session.scalar(stmt) == None:
        response = jsonify({"response":"No se encontraron ejercicios asociados a esa rutina"})
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    for i in session.scalars(stmt):
        d[str(i.ejercicio_id)] = {"nombre": i.nombre,
				  "repeticiones": i.repeticiones,
				  "duracion": i.duracion,
 				  "peso": i.peso}
    response = jsonify(d)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return(response)


@app.route('/rutinas', methods=['POST', 'OPTIONS'])
@cross_origin()
def crear_rutina():
    
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()

    elif request.method == 'POST':

        content = request.get_json()
        newRutina = Rutina(nombre = content["nombre"],
        grupo_muscular = content["grupo_muscular"])
        session.add(newRutina)
        session.commit()
        return _corsify_actual_response(jsonify({"status": 201}))
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))


@app.route('/rutinas', methods=['DELETE'])
def delete_rutina():
    rut_id = request.args.get('id')
    rut = session.get(Rutina,rut_id)
    if rut == None:
        print("NOOOOOOOOOOOOOOOOOOOO")
        return(jsonify({"status":"No existe la rutina"}))
    session.delete(rut)
    session.commit()
    response = Response(status = 201)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return(response)

@app.route('/rutina', methods=['GET'])
def get_rutina():
    rut_id = request.args.get('id')
    stmt = Select(Ejercicio).where(Ejercicio.rutina_id == rut_id)
    d = dict()
    return(jsonify({"a":"alo"}))
    #for i in session.scalars(stmt):


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080,debug=True)
