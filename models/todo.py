class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.estado = "pendiente"
        self.siguiente = None
        
class ListaTareas:
    def __init__(self):
        self.cabeza = None



    def agregar_tarea(self, descripcion):
        nuevo_nodo = Nodo(descripcion)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo_nodo



    def mostrar_tareas(self):
        actual = self.cabeza
        
        if actual is None:
            print("La lista está vacía.")
            return
        
        print("--- Lista de Tareas ---")
        
        while actual is not None:            
            print(f"[{actual.estado}] {actual.datos}")
            actual = actual.siguiente



    def marcar_completada(self, descripcion):
        actual = self.cabeza
            
        # Recorré la lista
        while actual is not None:
            if actual.datos == descripcion:
                actual.estado = "completada"
                print("Exito")  
                return                                
                                                
            actual = actual.siguiente

        print(f"Error: No se encontró la tarea '{descripcion}'.")

    def eliminar_tarea(self, descripcion):
        actual = self.cabeza
        anterior = None

        if actual is not None and actual.datos == descripcion:
            self.cabeza = actual.siguiente  
            print(f"Eliminada: {descripcion}")
            return


        while actual is not None and actual.datos != descripcion:
            anterior = actual     
            actual = actual.siguiente     

            
        if actual is None:
            print(f"No se encontró: {descripcion}")
            return


        anterior.siguiente = actual.siguiente 
        print(f"Eliminada: {descripcion}")






if __name__ == "__main__":
    lista = ListaTareas()
    lista.agregar_tarea("Tarea 1")
    lista.agregar_tarea("Tarea 2")
    lista.agregar_tarea("Tarea 3")
    
    print("Estado inicial:")
    lista.mostrar_tareas()
    
    lista.eliminar_tarea("Tarea 2")  # Eliminar del medio
    lista.eliminar_tarea("Tarea 1")  # Eliminar la cabeza
    lista.eliminar_tarea("Tarea Inexistente") # Probar caso negativo
    
    print("\nEstado final:")
    lista.mostrar_tareas()

