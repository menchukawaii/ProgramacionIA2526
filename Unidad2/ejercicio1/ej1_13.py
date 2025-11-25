c0 = int(input("introduce un numero entero, mayor que 0"))
pasos = 0
resultado = []
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1
    pasos += 1
    resultado.append(c0)
print(resultado)
