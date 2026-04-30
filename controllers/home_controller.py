from flask import render_template, request, redirect, url_for


from models.todo import ListaTareas
    

metodos = ListaTareas()


def index():
    """Renderiza la página principal con la lista de tareas obtenida del modelo y los métodos necesarios para mostrar el estado de cada tarea."""
    return render_template("index.html", tareas=metodos.obtener_todas(), metodos=metodos)


def agregar():
    """Agrega una nueva tarea a la lista utilizando la descripción obtenida del formulario y redirige a la página principal."""
    descripcion = request.form.get("descripcion")
    titulo = request.form.get("titulo")
    if descripcion and titulo:
        metodos.agregar_tarea(descripcion, titulo)
    return redirect(url_for("index"))


def completar():
    """Marca una tarea como completada utilizando la descripción obtenida del formulario y redirige a la página principal."""
    descripcion = request.form.get("descripcion")
    metodos.marcar_completada(descripcion)
    return redirect(url_for("index"))


def eliminar():
    """Elimina una tarea de la lista utilizando la descripción obtenida del formulario y redirige a la página principal."""
    descripcion = request.form.get("descripcion")
    metodos.eliminar_tarea(descripcion)
    return redirect(url_for("index"))