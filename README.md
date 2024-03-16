# Descripción:

# 1. Creación del repositorio:
- Crear un nuevo repositorio privado en GitHub llamado "GestorTareas".
- Clonar el repositorio en tu computadora local.
# 2. Estructura del proyecto:
- Crea un archivo README.md con la descripción del proyecto (Markdown).
- Crea un archivo tareas.py que contendrá la lógica del sistema.
# 3. Código Python:
```
# Importamos la librería datetime para manejar fechas
from datetime import datetime

# Definimos la estructura de datos para almacenar las tareas
tareas = []

# Función para agregar una nueva tarea
def agregar_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_limite = input("Ingrese la fecha límite (formato YYYY-MM-DD): ")
    tarea = {
        "descripcion": descripcion,
        "fecha_limite": datetime.strptime(fecha_limite, "%Y-%m-%d"),
        "estado": "pendiente",
    }
    tareas.append(tarea)

# Función para listar todas las tareas
def listar_tareas():
    for tarea in tareas:
        print(f"ID: {tareas.index(tarea)}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Fecha límite: {tarea['fecha_limite'].strftime('%Y-%m-%d')}")
        print(f"Estado: {tarea['estado']}")
        print("---")

# Función para completar una tarea
def completar_tarea():
    id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
    tareas[id_tarea]["estado"] = "completada"

# Función para eliminar una tarea
def eliminar_tarea():
    id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
    del tareas[id_tarea]

# Menú principal
while True:
    print("**Sistema de gestión de tareas**")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        listar_tareas()
    elif opcion == 3:
        completar_tarea()
    elif opcion == 4:
        eliminar_tarea()
    elif opcion == 5:
        break
    else:
        print("Opción no válida.")

print("¡Hasta luego!")
```
# Tareas:
- Agregar tareas:
    - Función para agregar nuevas tareas a una lista.
    - La función debe solicitar al usuario la descripción de la tarea y la fecha límite.
    - Almacenar las tareas en una estructura de datos adecuada (lista, diccionario, etc.).
- Listar tareas:
    - Función para mostrar todas las tareas almacenadas.
    - Mostrar la descripción, fecha límite y estado de cada tarea (pendiente, completada).
- Completar tareas:
    - Función para marcar una tarea como completada.
    - Solicitar al usuario el ID o la descripción de la tarea a completar.
- Eliminar tareas:
    - Función para eliminar una tarea de la lista.
    - Solicitar al usuario el ID o la descripción de la tarea a eliminar.
# 4. Control de versiones con Git:
- Agregar todos los archivos del proyecto al índice de Git.
- Realizar commits con mensajes descriptivos para cada cambio.
- Subir los cambios al repositorio remoto en GitHub.
# 5. Colaboración en GitHub:
- Crear una rama nueva para trabajar en una nueva función llamada "editar_tarea".
- Implementar la nueva función en la rama nueva.
- Enviar una solicitud de pull request (pull request) para fusionar la nueva rama con la rama principal.