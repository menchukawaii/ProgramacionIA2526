def calcula_media(estudiante, lista_estudiantes):
    estudiante_encontrado = None
    for i in lista_estudiantes:
        if i["nombre"] == estudiante:
            estudiante_encontrado = i
    if not estudiante_encontrado: raise ValueError("El estudiante no está en la lista") 

    notas = 0

    for asig in estudiante_encontrado["notas"]:
        notas += asig[1]

    return notas / len(estudiante_encontrado["notas"])


# codigo de prueba
if __name__ == "__main__":
    lista_estudiantes = [
        {
            "nombre": "Carmen",
            "notas": [("Matemáticas", 8.5), ("IA", 9.2), ("Programación", 7.8)]
        },
        {
            "nombre": "Juan",
            "notas": [("Matemáticas", 6.0), ("IA", 5.5), ("Programación", 4.0)]
        },
        {
            "nombre": "Elena",
            "notas": [("Matemáticas", 9.0), ("IA", 10.0), ("Programación", 9.5)]
        }
    ]
    print(calcula_media("Pepe", lista_estudiantes))