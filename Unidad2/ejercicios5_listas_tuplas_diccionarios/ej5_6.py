'''
===========================REGISTRO ASISTENCIA===========================

Se dispone de un diccionario con los datos de los estudiantes.
Cada estudiante tiene un nombre como clave en el diccionario.
El valor asociado es una lista de tuplas donde cada tupla contiene el nombre
de la asignatura (matemáticas, lengua, historia e inglés) , un valor booleano
que indica si asistió a clase y un valor de comportamiento que puede ser
“bueno”, “regular” o “malo”.

Tu tarea es desarrollar un sistema para registrar la asistencia y el
comportamiento de los alumnos en las clases. Debes generar un nuevo
diccionario que para cada estudiante, informe de su porcentaje de asistencia
y su comportamiento. El comportamiento será “malo” si el estudiante tiene
un comportamiento “malo” en más del 25% de las clases; en caso contrario el
comportamiento será “aceptable”

Recomendación: incluye una función para calcular el porcentaje de clases
a las que asistió cada estudiante y para verificar su comportamiento.
'''

registro_estudiantes = {
    "Ana García": [
        ("matemáticas", True, "bueno"),
        ("lengua", True, "regular"),
        ("historia", False, "bueno"),
        ("inglés", True, "malo")
    ],
    "Carlos López": [
        ("matemáticas", True, "bueno"),
        ("lengua", False, "malo"),
        ("historia", True, "regular"),
        ("inglés", True, "bueno")
    ],
    "Elena Torres": [
        ("matemáticas", True, "bueno"),
        ("lengua", True, "bueno"),
        ("historia", True, "bueno"),
        ("inglés", True, "bueno")
    ]
}

def calcular_porcentaje_asistencia(datos_estudiante):
    porcentaje_asistencia = 0
    for asignatura in datos_estudiante:
        porcentaje_asistencia +1 if asignatura[1]==True else porcentaje_asistencia
    return porcentaje_asistencia / len(datos_estudiante)

def evaluar_comportamiento(datos_estudiante):
    porcentaje = 0
    comportamiento = ""
    for asignatura in datos_estudiante:
        porcentaje +1 if asignatura[2]=="malo" else porcentaje
    porcentaje = porcentaje/ len(datos_estudiante)
    comportamiento = "malo" if porcentaje >= 0.5 else "aceptable"
    return comportamiento

def crear_registro_actualizado(registro_estudiantes):
    nuevo_registro = {}
    for key, value in registro_estudiantes.items():
        nuevo_registro[key] = [
            calcular_porcentaje_asistencia(value),
            evaluar_comportamiento[value]
            ]
    return nuevo_registro
        

print(crear_registro_actualizado(registro_estudiantes))















        



