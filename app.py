from flask import Flask
from controllers.home_controller import index, agregar, completar, eliminar

app = Flask(__name__)


app.add_url_rule("/", view_func=index)
app.add_url_rule("/agregar", view_func=agregar, methods=["POST"])
app.add_url_rule("/completar", view_func=completar, methods=["POST"])
app.add_url_rule("/eliminar", view_func=eliminar, methods=["POST"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)