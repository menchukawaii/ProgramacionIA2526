def calcula_media(estudiante):
    tuplas_asignaturas = estudiante["notas"]
    notas = 0
    for i in tuplas_asignaturas:
        notas += i[1]
    return notas/len(tuplas_asignaturas)

e =     {
        "nombre": "Carmen",
        "notas": [("Matemáticas", 8.5), ("IA", 9.2), ("Programación", 7.8)]
    }
print(calcula_media(e))