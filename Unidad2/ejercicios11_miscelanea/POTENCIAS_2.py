def potencias(n, npot = 2):
    for i in range(npot):
        yield f"{n}**{i} = {n**i}"

for i in potencias(2, 4):
    print(i)