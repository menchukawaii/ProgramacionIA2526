lista = [5,8,5,5,8,7,6,1,3,4,7,6,5,4,2]

for i in range(len(lista)):
    # recorremos el array comparando cada valor con el siguiente,
    #tantas veces como valores tenga el array para asegurarnos de que
    #todos los valores puedan desplazarse a su posición adecuada
    for j in range(0, len(lista) - i - 1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
print(lista) 
