from os import strerror


try:
    stream = open("Unidad2/ejercicios10_ficheros/ej10_5/manolita.txt", "wt")
    for i in range(10):
        stream.write(f"Linea {i}\n")
    stream.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))