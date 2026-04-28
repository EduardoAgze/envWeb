from flask import render_template, request, redirect, url_for


from models.todo import ListaTareas
    

lista_tareas = ListaTareas()


def index():
    """Renderiza la página principal con la lista de tareas obtenida del modelo."""
    return render_template("index.html", tareas=lista_tareas.obtener_todas())


def agregar():
    """Agrega una nueva tarea a la lista utilizando la descripción obtenida del formulario y redirige a la página principal."""
    descripcion = request.form.get("descripcion")  
    if descripcion:
        lista_tareas.agregar_tarea(descripcion)   
    return redirect(url_for("index"))


def completar():
    """Marca una tarea como completada utilizando la descripción obtenida del formulario y redirige a la página principal."""
    descripcion = request.form.get("descripcion")
    lista_tareas.marcar_completada(descripcion)
    return redirect(url_for("index"))


def eliminar():
    """Elimina una tarea de la lista utilizando la descripción obtenida del formulario y redirige a la página principal."""
    descripcion = request.form.get("descripcion")
    lista_tareas.eliminar_tarea(descripcion)
    return redirect(url_for("index"))