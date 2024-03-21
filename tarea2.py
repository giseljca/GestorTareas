# Función para editar una tarea
def editar_tarea():
    id_tarea = int(input("Ingrese el ID de la tarea a editar: "))
    nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
    if id_tarea >= 0 and id_tarea < len(tareas):
        tareas[id_tarea]["descripcion"] = nueva_descripcion
        print("Tarea editada correctamente.")
    else:
        print("ID de tarea no válido.")