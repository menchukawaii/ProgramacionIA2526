from os import strerror
import os

print("Python está buscando en:", os.getcwd())

try:
    # Abre el stream
    stream = open("Unidad2/ejercicios10_ficheros/ej10_2/carmen.txt", "rt")
    #Realiza el tratamiento del archivo
    contenido = stream.read()
    print(contenido)
    # Cierra el stream
    stream.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))