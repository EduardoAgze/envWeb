from flask import render_template, request, redirect, url_for


from models.todo import ListaTareas
    

lista_tareas = ListaTareas()


def index():
    return render_template("index.html", tareas=lista_tareas.obtener_todas())


def agregar():
    descripcion = request.form.get("descripcion")  
    if descripcion:
        lista_tareas.agregar_tarea(descripcion)   
    return redirect(url_for("index"))


def completar():
    descripcion = request.form.get("descripcion")
    lista_tareas.marcar_completada(descripcion)
    return redirect(url_for("index"))


def eliminar():
    descripcion = request.form.get("descripcion")
    lista_tareas.eliminar_tarea(descripcion)
    return redirect(url_for("index"))