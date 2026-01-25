from notas.estudiantes import lista_estudiantes
from notas.promedio import calcula_media

def consultar_nota():
    nombre = input("Introduce el nombre del estudiante")
    try:
        estudiante_encontrado = None
        for e in lista_estudiantes:
            if e["nombre"] == nombre:
                estudiante_encontrado = e
                break
        if not estudiante_encontrado:
            raise ValueError(f"Estudiante '{nombre}' no encontrado en el sistema.")
        media = calcula_media(estudiante_encontrado)
    except ValueError as e:
        print(f"Error de búsqueda: {e}")


