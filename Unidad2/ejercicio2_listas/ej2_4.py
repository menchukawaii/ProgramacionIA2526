lista = [8,4,1,3,6,9,7,4,5,2,1,0]

#manera 1
mayor1 = 0
for i in range(len(lista)):
    if lista[i] > mayor1:
        mayor1 = lista[i]
print(f"Manera 1 mayor = {mayor1}")

#manera 2
mayor2 = 0
for i in lista:
    if i > mayor2:
        mayor2 = i
print(f"Manera 2 mayor = {mayor2}")
    
