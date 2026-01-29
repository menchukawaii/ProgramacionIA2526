from os import strerror


try:
    stream = open(f"Unidad2/ejercicios10_ficheros/ej10_7/calificaciones.txt", "rt")
    #contar suma de las notas de cada alumno
    lineas = stream.readlines()
    lista = {}
    for i in lineas:
        partes = i.split()
        nombre = f"{partes[0]} {partes[1]}"
        nota = float(partes[2])
        
        if nombre not in lista:
            lista[nombre] = nota
        else:
            lista[nombre] += nota
    print(lista)
    stream.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))