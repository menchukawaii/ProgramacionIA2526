from os import strerror

try:


    # Abre el stream
    stream = open("prim.txt", mode = "rt")
    #Realiza el tratamiento del archivo
    print(stream.read())
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