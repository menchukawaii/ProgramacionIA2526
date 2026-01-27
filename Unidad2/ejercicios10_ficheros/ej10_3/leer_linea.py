from os import strerror

try:
    # Abre el stream
    stream = open("Unidad2/ejercicios10_ficheros/ej10_3/carmen.txt", "rt")

    #Realiza el tratamiento del archivo
    contenido = stream.readline()
    print(contenido)
    contenido = stream.readline()
    print(contenido)
    contenido = stream.readline()
    print(contenido)

    lineas = contenido.splitlines()
    numero_de_lineas = len(lineas)
    print(numero_de_lineas)
    
    # Cierra el stream
    stream.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))