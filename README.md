# Fit-n-Strong

**Endpoints**

Ruta: http://20.226.52.146:8080/rutinas Método: *GET*

*Descripción*: Devuelve un JSON que contiene todos las rutinas disponibles,

Ruta: http://20.226.52.146:8080/rutinas?rut_id=<id_rutina_que_pertenece> Método: *GET*

*Descripción*: Devuelve un JSON que contiene todos los ejercicos que pertenezcan a la rutina asociada con id = rut_id

Ruta: http://20.226.52.146:8080/rutinas Método: *POST*

*Descripción*: Crea en la BD una rutina

Ruta: http://20.226.52.146:8080/rutinas?rut_id<id_rutina_a_borrar> Método: *DELETE*

*Descripción*: Elimina una rutina de la BD y todos sus ejercicios
