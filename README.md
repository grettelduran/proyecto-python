# taller5-python
Este sera el proyecto servidor de python para el taller 5 donde se podra ver todos los jugadores y agregar nuevos jugadores con validaciones

modelo.py contiene la clase Player la cual sera lo que se serializara/deserializara a JSON.
basedatos.py contiene la clase BaseDatos que maneja la lectura y escritura al archivo json de usuarios existentes.
controller.py contiene la creacion de objetos Player en base a los parametros enviados desde el Rest Api.
main.py contiene el Rest Api que se encarga de llamar al controlador
