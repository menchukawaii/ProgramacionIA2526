##comprobar si es triangulo rectangulo
def es_triangulo(lado1, lado2, lado3):
    return ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado3 + lado2) > lado1)

def es_triangulo_rectangulo(lado1, lado2, lado3):
    if es_triangulo(lado1, lado2, lado3):
        if (lado1**2) + (lado2**2) == lado3**2:
            return True
        elif (lado1**2) + (lado3**2) == lado2**2:
            return True
        elif (lado3**2) + (lado2**2) == lado1**2:
            return True
        else:
            return False
    else:
        return False

print(es_triangulo(2,2,2))
print(es_triangulo(2,0,2))

print(es_triangulo_rectangulo(2,2,2))
print(es_triangulo_rectangulo(3,4,5))
