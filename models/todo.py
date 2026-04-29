class Nodo:
    """Representa un nodo en la lista enlazada """
    def __init__(self, datos):
        """Inicializa un nodo con sus datos y el estado "pendiente" """
        self.datos = datos
        self.estado = "pendiente"
        self.siguiente = None
        
class ListaTareas:
    """Representa la lista enlazada de tareas """
    def __init__(self):
        """inicializa la lista con la cabeza en None """
        self.cabeza = None



    def agregar_tarea(self, descripcion):
        """Agrega una nueva tarea al final de la lista """
        nuevo_nodo = Nodo(descripcion)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo_nodo



    def marcar_completada(self, descripcion):
        """Marca una tarea como completada buscando por su descripción,si no encuentra pasa al sgte nodo."""
        actual = self.cabeza
            
        while actual is not None:
            if actual.datos == descripcion:
                if actual.estado == "completada":
                    actual.estado = "pendiente"
                    return
                else:
                    actual.estado = "completada"  
                    return                                
                                                
            actual = actual.siguiente





    def eliminar_tarea(self, descripcion):
        """Elimina una tarea de la lista buscando por su descripción, verificando si es la cabeza 
            o si se encuentra en el medio o al final de la lista."""
        actual = self.cabeza
        anterior = None

        if actual is not None and actual.datos == descripcion:
            self.cabeza = actual.siguiente  
            return


        while actual is not None and actual.datos != descripcion:
            anterior = actual     
            actual = actual.siguiente   

        if actual is not None:
            anterior.siguiente = actual.siguiente
        



    def obtener_todas(self):
        """Obtiene todas las tareas en la lista y las devuelve como una lista de diccionarios con su descripción y estado."""
        resultado = []
        
        actual = self.cabeza
        
        while actual is not None:
            tarea = {"datos": actual.datos,"estado": actual.estado}
            resultado.append(tarea)
            actual = actual.siguiente
        return resultado
        

