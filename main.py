import mysql.connector
from mysql.connector import Error


from typing import List
from typing import Optional


from flask import Flask,jsonify,request








from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def_error_msg = "Error while connecting to MySQL"

try: 
    connection = mysql.connector.connect(host = 'localhost',
                                         database = 'fitstrong',
                                         user = 'fit',
                                         password = 'Testing_2023')
    if connection.is_connected:
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print (record)
except Error as e:
    print(def_error_msg, e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()    


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
    d = None
    c = 0
    try: 
        connection = mysql.connector.connect(host = 'localhost',
                                            database = 'fitstrong',
                                            user = 'fit',
                                            password = 'Testing_2023')
        if connection.is_connected:
            query = """select * from rutina where rutina_id = %s"""
            cursor = connection.cursor()
            cursor.execute(query,(id_rutina,))
            record = cursor.fetchone()
            if len(record) != 0: 
                d = {"nombre": record[1], "grupo_muscular": record[2]}
    except Error as e:
        print(def_error_msg, e)
        return _corsify_actual_response(jsonify({"status":500}))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()  
            c = 1
    if d == None and c == 0:
        return _corsify_actual_response(jsonify({"status": 500})) 
    elif d == None and c == 1:
        return _corsify_actual_response(jsonify({"response": "No hay rutina"})) 
    return _corsify_actual_response(jsonify(d))


@app.route('/ejercicio', methods=['GET'])
def get_ejercicio():
    id_ejercicio = request.args.get("id")
    d = None
    c = 0
    try: 
        connection = mysql.connector.connect(host = 'localhost',
                                            database = 'fitstrong',
                                            user = 'fit',
                                            password = 'Testing_2023')
        if connection.is_connected:
            query = """select * from ejercicio where ejercicio_id = %s"""
            cursor = connection.cursor()
            cursor.execute(query,(id_ejercicio,))
            record = cursor.fetchone()
            if len(record) != 0:
                d = {"ejercicio_id": record[0],"nombre": record[1], 
                     "repeticiones": record[2], "duracion": record[3], "peso": record[4]}
    except Error as e:
        print("Error while connecting to MySQL", e)
        return _corsify_actual_response(jsonify({"status": 500}))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            c = 1 
    if d == None and c == 0:
        return _corsify_actual_response(jsonify({"status": 500})) 
    elif d == None and c == 1:
        return _corsify_actual_response(jsonify({"response": "No hay ejercicio"})) 
    return _corsify_actual_response(jsonify(d))


@app.route('/rutinas', methods=['GET'])
def get_rutinas():
    d = list()
    c = 0
    try: 
        connection = mysql.connector.connect(host = 'localhost',
                                            database = 'fitstrong',
                                            user = 'fit',
                                            password = 'Testing_2023')
        if connection.is_connected:
            query = "select * from rutina"
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()

            if len(records) != 0:
                for record in records:
                    l = {"id": record[0],"nombre": record[1], "grupo_muscular": record[2]}
                    d.append(l)
    except Error as e:
        print(def_error_msg, e)
        return _corsify_actual_response(jsonify({"status": 500}))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close() 
            c = 1
    if len(d) == 0 and c == 0:
        return _corsify_actual_response(jsonify({"status": 500})) 
    elif len(d) == 0 and c == 1:
        return _corsify_actual_response(jsonify({"response": "No hay rutinas"})) 
    return _corsify_actual_response(jsonify(d))

@app.route('/ejercicios', methods=['GET'])
def get_ejercicios_by_rutina():
    rut_id = request.args.get("id")
    d = list()
    c = 0
    try: 
        connection = mysql.connector.connect(host = 'localhost',
                                            database = 'fitstrong',
                                            user = 'fit',
                                            password = 'Testing_2023')
        if connection.is_connected:
            query = """select * from ejercicio where rutina_id = %s"""
            cursor = connection.cursor()
            
            cursor.execute(query,(rut_id,))
            records = cursor.fetchall()
            if len(records) != 0:
                for record in records:
                    l = {"ejercicio_id": record[0],
                         "nombre": record[1], "repeticiones": record[2],
                        "duracion": record[3], "peso": record[4]}
                    d.append(l)
    except Error as e:
        print(def_error_msg, e)
        return _corsify_actual_response(jsonify({"status": 500}))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close() 
            c = 1
    if len(d) == 0 or c == 0:
        print("CASO 1")
        return _corsify_actual_response(jsonify({})) 
    """elif len(d) == 0 and c == 1:
        print("CASO 2"  )
        return _corsify_actual_response(jsonify({"response": "No hay ejercicios"})) 
    """
    return _corsify_actual_response(jsonify(d))



@app.route('/rutinas', methods=['POST', 'OPTIONS','DELETE'])
@cross_origin()
def crear_rutina():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    elif request.method == 'DELETE':
        rut_id = request.args.get('id')
        d = 0
        try: 
            connection = mysql.connector.connect(host = 'localhost',
                                                database = 'fitstrong',
                                                user = 'fit',
                                                password = 'Testing_2023')
            if connection.is_connected:
                query = """delete  from rutina where rutina_id = %s"""
                cursor = connection.cursor()
                cursor.execute(query,(int(rut_id),))
                connection.commit()
        except Error as e:
            print("Error while connecting to MySQL", e)
            return _corsify_actual_response(jsonify({"status": 500}))
        finally:
            if connection.is_connected():
                d = 1
                cursor.close()
                connection.close() 
        if d == 0:
            return _corsify_actual_response(jsonify({"status": 500})) 
        return _corsify_actual_response(jsonify({"status": 200}))

    elif request.method == 'POST':
        content = request.get_json()
        d = 0
        try: 
            connection = mysql.connector.connect(host = 'localhost',
                                                database = 'fitstrong',
                                                user = 'fit',
                                                password = 'Testing_2023')
            if connection.is_connected:
                query = """insert into rutina (nombre, grupo_muscular) values (%s, %s)"""
                cursor = connection.cursor()
                record = (content["nombre"], content["grupo_muscular"],)
                cursor.execute(query,record)
                connection.commit()
                cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)
            return _corsify_actual_response(jsonify({"status": 500}))
        finally:
            if connection.is_connected():
                d = 1
                connection.close() 
        if d == 0:
            return _corsify_actual_response(jsonify({"status": 500})) 
        return _corsify_actual_response(jsonify({"status": 200}))


    else:
       raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))
    
@app.route('/ejercicios', methods=['POST', 'OPTIONS','DELETE'])
@cross_origin()
def crear_ejercicio():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()

    elif request.method == 'DELETE':
        rut_id = request.args.get('id') 
        d = 0
        try: 
            connection = mysql.connector.connect(host = 'localhost',
                                                database = 'fitstrong',
                                                user = 'fit',
                                                password = 'Testing_2023')
            if connection.is_connected:
                query = """delete  from ejercicio where ejercicio_id = %s"""
                cursor = connection.cursor()
                cursor.execute(query,(int(rut_id),))
                connection.commit()
        except Error as e:
            print("Error while connecting to MySQL", e)
            return _corsify_actual_response(jsonify({"status": 500}))
        finally:
            if connection.is_connected():
                d = 1
                cursor.close()
                connection.close() 
        if d == 0:
            return _corsify_actual_response(jsonify({"status": 500})) 
        return _corsify_actual_response(jsonify({"status": 200}))

    elif request.method == 'POST':

        content = request.get_json()
        if "rutina_id" not in content:
            return(jsonify({"Respuesta":"No se añadio la rutina a la que pertence"}))
        rutina_id = content["rutina_id"]
        nombre = ""
        repeticiones = ""
        duracion = ""
        peso = ""
        if "nombre" in content:
            nombre = content["nombre"]
        if "repeticiones" in content:
            repeticiones = content["repeticiones"]
        if "duracion" in content:
            duracion = content["duracion"]
        if "peso" in content:
            peso = content["peso"]  
        d = 0
        try: 
            connection = mysql.connector.connect(host = 'localhost',
                                                database = 'fitstrong',
                                                user = 'fit',
                                                password = 'Testing_2023')
            if connection.is_connected:
                query = """insert into ejercicio (nombre, repeticiones, duracion,peso, rutina_id) values (%s, %s, %s, %s, %s)"""
                cursor = connection.cursor()
                record = (nombre, int(repeticiones), duracion, int(peso), int(rutina_id),)
                cursor.execute(query,record)
                connection.commit()
                cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)
            return _corsify_actual_response(jsonify({"status": 500}))
        finally:
            if connection.is_connected():
                d = 1
                connection.close() 
        if d == 0:
            return _corsify_actual_response(jsonify({"status": 500})) 
        return _corsify_actual_response(jsonify({"status": 200}))

    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))



@app.route('/rutinas', methods=['PUT'])
def update_rutina():
    content = request.get_json()
    if "rutina_id" not in content:
        return(jsonify({"Respuesta":"No se añadió el id de la rutina"}))
    id_rutina = content["rutina_id"]
    nombre = ""
    grupo_muscular = ""

    if "nombre" in content:
        nombre = content["nombre"]
    if "grupo_muscular" in content:
        grupo_muscular = content["grupo_muscular"]
    d = None
    c = 0
    try: 
        connection = mysql.connector.connect(host = 'localhost',
                                            database = 'fitstrong',
                                            user = 'fit',
                                            password = 'Testing_2023')
        if connection.is_connected:
            query = """select * from rutina where rutina_id = %s"""
            cursor = connection.cursor()
            cursor.execute(query,(id_rutina,))
            record = cursor.fetchone()
            if len(record) != 0: 
                d = {"nombre": record[1], "grupo_muscular": record[2]}
    except Error as e:
        print(def_error_msg, e)
        return _corsify_actual_response(jsonify({"status":500}))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()  
            c = 1
    if d == None and c == 0:
        return _corsify_actual_response(jsonify({"status": 500})) 
    elif d == None and c == 1:
        return _corsify_actual_response(jsonify({"response": "No hay rutina"})) 

    if nombre == "":
        nombre = d["nombre"]
    if grupo_muscular == "":
        grupo_muscular = d["grupo_muscular"]

    c = 0
    try: 
        connection = mysql.connector.connect(host = 'localhost',
                                            database = 'fitstrong',
                                            user = 'fit',
                                            password = 'Testing_2023')
        if connection.is_connected:
            query = """update rutina set nombre = %s, grupo_muscular = %s
                where rutina_id = %s"""
            record = (nombre,grupo_muscular,id_rutina,)
            cursor = connection.cursor()
            cursor.execute(query,record)
            connection.commit()
    except Error as e:
        print(def_error_msg, e)
        return _corsify_actual_response(jsonify({"status":500}))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()  
            c = 1
    if c == 0:
        return _corsify_actual_response(jsonify({"status": 500})) 
    return _corsify_actual_response(jsonify({"status":200}))




@app.route('/ejercicios', methods=['PUT'])
def update_ejercicio():
    content = request.get_json()

    if "ejercicio_id" not in content:
        return(jsonify({"Respuesta":"No se añadió el id de la rutina"}))

    id_ejercicio = content["ejercicio_id"]
    nombre = ""
    repeticiones = ""
    duracion = ""
    peso = ""

    if "nombre" in content:
        nombre = content["nombre"]
    if "repeticiones" in content:
        repeticiones = content["repeticiones"]
    if "duracion" in content:
        duracion = content["duracion"]
    if "peso" in content:
        peso = content["peso"]
    d = None
    c = 0
    try: 
        connection = mysql.connector.connect(host = 'localhost',
                                            database = 'fitstrong',
                                            user = 'fit',
                                            password = 'Testing_2023')
        if connection.is_connected:
            query = """select * from ejercicio where ejercicio_id = %s"""
            cursor = connection.cursor()
            cursor.execute(query,(id_ejercicio,))
            record = cursor.fetchone()
            if len(record) != 0: 
                d = {"nombre": record[1], "repeticiones": record[2],
                    "duracion": record[3], "peso": record[4]}
    except Error as e:
        print(def_error_msg, e)
        return _corsify_actual_response(jsonify({"status":500}))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()  
            c = 1
    if d == None and c == 0:
        return _corsify_actual_response(jsonify({"status": 500})) 
    elif d == None and c == 1:
        return _corsify_actual_response(jsonify({"response": "No hay rutina"})) 

    if nombre == "":
        nombre = d["nombre"]
    if repeticiones == "":
        repeticiones = d["grupo_muscular"]
    if duracion == "":
        duracion = d["duracion"]
    if peso == "":
        peso = d["peso"]

    c = 0
    try: 
        connection = mysql.connector.connect(host = 'localhost',
                                            database = 'fitstrong',
                                            user = 'fit',
                                            password = 'Testing_2023')
        if connection.is_connected:
            query = """update ejercicio set nombre = %s, repeticiones = %s,
                duracion = %s, peso = %s where ejercicio_id = %s"""
            record = (nombre,repeticiones, duracion, peso, id_ejercicio,)
            cursor = connection.cursor()
            cursor.execute(query,record)
            connection.commit()
    except Error as e:
        print(def_error_msg, e)
        return _corsify_actual_response(jsonify({"status":500}))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()  
            c = 1
    if c == 0:
        return _corsify_actual_response(jsonify({"status": 500})) 
    return _corsify_actual_response(jsonify({"status":200}))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080,debug=True)
