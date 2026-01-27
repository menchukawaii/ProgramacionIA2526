from os import strerror

try:
    # Abre el stream
    stream = open("Unidad2/ejercicios10_ficheros/ej10_3/carmen.txt", "rt")

    #Realiza el tratamiento del archivo
    contenido = stream.readlines() #en plural!!!!!!!!
    print(contenido)

    if len(contenido) == 0:
        print("El archivo está vacío.")
    else:
        total_caracteres = 0
        for linea in contenido:
            print(linea, end="")  # end="" porque la línea ya trae su \n
            total_caracteres += len(linea)
        print(total_caracteres)
        
    # Cierra el stream
    stream.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

 