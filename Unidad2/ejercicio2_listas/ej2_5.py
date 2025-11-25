lista = [5,4,7,2,3,1,4,5,6,9,8,5,2,1,4,7,5,3,2,1,5,6]
sin_repetidos = []
for i in lista:
    if i not in sin_repetidos:
        sin_repetidos.append(i)
print(lista)
print(sin_repetidos)
