from os import strerror

try:


    # Abre el stream
    #stream = open("prim.txt", mode = "rt") # busca en / de la carpeta en la que estoy, osea ProgramacionIA2526
    stream = open("Unidad2/ejercicios10_ficheros/ej10_2/carmen.txt", "rt")
    #Realiza el tratamiento del archivo
    caracter = stream.read(1)
    contador = 0
    while caracter != "":
        contador +=1
        print(caracter, end="")
        caracter = stream.read(1)
    print(contador)
    # Cierra el stream
    stream.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))