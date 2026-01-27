from notas.estudiantes import lista_estudiantes
from notas.promedio import calcula_media

def consultar_nota(lista_estudiantes):
    nombre = input("Introduce el nombre del estudiante")
    try:
        media = calcula_media(nombre, lista_estudiantes)
        print(f"La nota media de {nombre} es {media}")
    except ValueError as e:
        print(f"Error : {e}")

consultar_nota(lista_estudiantes)
