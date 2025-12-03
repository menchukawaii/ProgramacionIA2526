'''
==============================EXPEDIENTE ALUMNO==============================

En tu programa dispones** de las calificaciones obtenidas por Pedro en cada uno
de las cuatro asignaturas que está estudiando en esta evaluación: lengua, matemáticas,
física e inglés. De cada asignatura se dispone de las calificaciones de todas las
pruebas realizadas hasta el momento por Pedro.

* No es necesario que incluyas ningún método para obtener esta información.
Está disponible en el código del programa.

Tu programa debe mostrar las notas obtenidas por Pedro en cada asignatura,
y la nota media por asignatura (muestra la calificación con dos decimales).
Haz una función que calcule la nota media.
'''

NOTAS = {
    "matenaticas": 7.8,
    "lengua": 5.4,
    "fisica": 3.4,
    "ingles": 10
    }

def calcular_media(notas):
    media = 0
    for clave, valor in notas.items():
        media += valor
    return round(media / (len(notas)+1), 2)

print(NOTAS)
print(calcular_media(NOTAS))
