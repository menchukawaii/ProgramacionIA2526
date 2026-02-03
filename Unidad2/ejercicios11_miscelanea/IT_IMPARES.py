class ImparesError (ValueError):
    pass


def impares (n, primer = 1):
    contador = 0
    valor = primer
    while contador < n:
        yield valor
        contador += 1
        valor += 2


for i in impares(4):
    print(i, end=" ")