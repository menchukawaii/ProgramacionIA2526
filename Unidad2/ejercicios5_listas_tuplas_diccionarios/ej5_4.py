'''
===========================CALIFCACIONES ALUMNO===========================

Tu tarea es crear un diccionario que contenga para cada uno de los estudiantes
del curso su nota media. Se dispone de un diccionario que tiene como clave
el nombre del alumno y como valor una lista de tuplas.
Cada tupla contiene el nombre de la asignatura (matemáticas, lengua, historia
e inglés) y su calificación.

Modifica ahora el programa para que el diccionario generado contenga,
para cada alumno, además de su nota media, la asignatura en la que obtuvo
la mayor calificación.
'''

calificaciones_alumnos = {
    "Ana García": [
        ("matemáticas", 8.5),
        ("lengua", 7.0),
        ("historia", 9.2),
        ("inglés", 8.8)
    ],
    "Carlos López": [
        ("matemáticas", 6.0),
        ("lengua", 7.5),
        ("historia", 5.5),
        ("inglés", 6.5)
    ],
    "Elena Torres": [
        ("matemáticas", 9.5),
        ("lengua", 9.0),
        ("historia", 10.0),
        ("inglés", 9.8)
    ]
}

def calcular_nota_media(calificaciones_alumnos):
    nota_media = {}
    for key, value in calificaciones_alumnos.items():
        media = 0
        for asignatura in value:
           media += asignatura[1]
        media = media / len(value)
        nota_media[key] = media
    return nota_media

def add_mayor_calificacion(nota_media, calificaciones_alumnos):
    mayor_calificacion = {}
    for key, value in calificaciones_alumnos.items():
        mayor = 0
        for asignatura in value:
           mayor = asignatura[1] if asignatura[1] > mayor else mayor
        mayor_calificacion[key] = mayor

    for key, value in nota_media.items():
        nota_media[key] = [value]
        nota_media[key].append(mayor_calificacion[key])

    return nota_media

nota_media = calcular_nota_media(calificaciones_alumnos)
print(nota_media)
print(add_mayor_calificacion(nota_media, calificaciones_alumnos))















    
