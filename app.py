from flask import Flask
from controllers.home_controller import index, agregar, completar, eliminar

# Archivo principal de la aplicación Flask, que configura las rutas y ejecuta el servidor.
app = Flask(__name__)

"""Configura las rutas de la aplicación Flask para las operaciones de la lista de tareas, 
    asignando las funciones del controlador a cada ruta correspondiente."""
app.add_url_rule("/", view_func=index)
app.add_url_rule("/agregar", view_func=agregar, methods=["POST"])
app.add_url_rule("/completar", view_func=completar, methods=["POST"])
app.add_url_rule("/eliminar", view_func=eliminar, methods=["POST"])

# Inicia la aplicación Flask en el host, en el port:8000 y con debug activado.
if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=8000, debug=True)
    
#implementar lo de abajo |
#                        v
#import os               
#app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))