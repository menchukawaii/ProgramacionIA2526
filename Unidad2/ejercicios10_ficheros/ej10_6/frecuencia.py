from os import strerror


try:
    # archivo = input("Introduce el nombre del archivo")
    # stream = open(f"Unidad2/ejercicios10_ficheros/ej10_6/{archivo}", "rt")
    stream = open(f"Unidad2/ejercicios10_ficheros/ej10_6/archivo1.txt", "rt")
    
    # print(f"Total de caracteres: {len(stream)}")
    abecedario = {}
    caracter = stream.read(1)
    while caracter != "":
        caracter = caracter.lower()
        if caracter in abecedario:
            abecedario[caracter] += 1
        else:
            abecedario[caracter] = 1
        caracter = stream.read(1)
    print(abecedario)
    stream.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))