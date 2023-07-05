from fastapi import FastAPI
import pg8000
from pg8000 import ProgrammingError
app = FastAPI()

# Configuración de la conexión a la base de datos
conn = pg8000.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)
cursor = conn.cursor()


@app.exception_handler(ProgrammingError)
async def pg8000_exception_handler(request, exc):
    return {"error": str(exc), "message": "Error en la base de datos"}


@app.get("/ejercicios")
def get_ejercicios():
    try:
        # Obtener todos los ejercicios de la base de datos
        cursor.execute("SELECT * FROM ejercicio")
        ejercicios = cursor.fetchall()
        return {"ejercicios": ejercicios}
    except ProgrammingError as e:
        raise e


@app.get("/ejercicios/{ejercicio_id}")
def get_ejercicio(ejercicio_id: int):
    try:
        # Obtener un ejercicio específico por su ID
        cursor.execute("SELECT * FROM ejercicio WHERE ejercicio_id = %s", (ejercicio_id,))
        ejercicio = cursor.fetchone()
        if ejercicio is None:
            return {"error": "Ejercicio no encontrado"}
        return {"ejercicio": ejercicio}
    except ProgrammingError as e:
        raise e


@app.post("/ejercicios")
def create_ejercicio(nombre: str, repeticiones: int, duracion: str, peso: int, rutina_id: int):
    try:
        # Crear un nuevo ejercicio en la base de datos
        cursor.execute("INSERT INTO ejercicio (nombre, repeticiones, duracion, peso, rutina_id) "
                       "VALUES (%s, %s, %s, %s, %s) RETURNING ejercicio_id",
                       (nombre, repeticiones, duracion, peso, rutina_id))
        ejercicio_id = cursor.fetchone()[0]
        conn.commit()
        return {"ejercicio_id": ejercicio_id, "message": "Ejercicio creado exitosamente"}
    except ProgrammingError as e:
        raise e


@app.put("/ejercicios/{ejercicio_id}")
def update_ejercicio(ejercicio_id: int, nombre: str = None, repeticiones: int = None, duracion: str = None,
                     peso: int = None, rutina_id: int = None):
    try:
        # Actualizar un ejercicio existente en la base de datos
        update_fields = []
        params = []
        if nombre is not None:
            update_fields.append("nombre = %s")
            params.append(nombre)
        if repeticiones is not None:
            update_fields.append("repeticiones = %s")
            params.append(repeticiones)
        if duracion is not None:
            update_fields.append("duracion = %s")
            params.append(duracion)
        if peso is not None:
            update_fields.append("peso = %s")
            params.append(peso)
        if rutina_id is not None:
            update_fields.append("rutina_id = %s")
            params.append(rutina_id)

        if not update_fields:
            return {"error": "Nada para actualizar"}

        update_query = "UPDATE ejercicio SET " + ", ".join(update_fields) + " WHERE ejercicio_id = %s"
        params.append(ejercicio_id)
        cursor.execute(update_query, tuple(params))
        conn.commit()
        return {"message": "Ejercicio actualizado exitosamente"}
    except ProgrammingError as e:
        raise e


@app.delete("/ejercicios/{ejercicio_id}")
def delete_ejercicio(ejercicio_id: int):
    try:
        # Eliminar un ejercicio de la base de datos
        cursor.execute("DELETE FROM ejercicio WHERE ejercicio_id = %s", (ejercicio_id,))
        conn.commit()
        return {"message": "Ejercicio eliminado exitosamente"}
    except ProgrammingError as e:
        raise e


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
