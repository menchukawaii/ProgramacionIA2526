bloques = int(input("introduce el numero de bloques"))
nfilas = 0
for i in range (1, bloques + 1):
    if bloques <= nfilas:
        break
    bloques -= i
    nfilas += 1
print(f"Altura: {nfilas}")
