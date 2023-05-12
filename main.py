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

app = Flask(__name__)

@app.route('/rutinas', methods=['OPTIONS'])
def reply_headers():
    a = jsonify({"a":"1"})
    a.headers['Access-Control-Allow-Headers'] = "content_type"
    a.headers['Access-Control-Allow-Origin'] = '*'
   # a.headers['Content-Type'] = "text/plain"
    a.headers['Access-Control-Allow-Methods'] = "PUT, GET, POST, DELETE, OPTIONS"
    return a

@app.route('/rutinas', methods=['GET'])
def get_rutinas():
    #content = request.json()
    stmt = Select(Rutina)
    d = dict()
    if session.scalar(stmt) == None:
        response = jsonify({"response": "No hay rutina"})
        response.headers['Access-Control-Allow-Origin'] = '*'
    for i in session.scalars(stmt):
        d[str(i.rutina_id)] = {"nombre": str(i.nombre), "grupo_muscular": str(i.grupo_muscular)}

    response = jsonify(d)
    response.headers['Access-Control-Allow-Origin'] = '*'
    #print(a)
    return(response)

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

@app.route('/rutinas', methods=['POST'])
def crear_rutina():
    content = request.get_json()
    newRutina = Rutina(nombre = content["nombre"],
	grupo_muscular = content["grupo_muscular"])
    session.add(newRutina)
    session.commit()
    response = jsonify({"status":201})
   # response.headers['Content-Type'] = "text/plain"
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = "PUT, GET, POST, DELETE, OPTIONS"
    return(response)

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
