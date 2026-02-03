def tabla_multiplicar(n):
    for i in range(1, 11):
        yield f"{n} * {i} = {n*i}"

for i in tabla_multiplicar(7):
    print(i, sep="\n")