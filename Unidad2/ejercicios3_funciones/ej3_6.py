## area del triangulo
import math

def es_triangulo(lado1, lado2, lado3):
    return ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado3 + lado2) > lado1)

def calcular_area(lado1, lado2, lado3):
    if es_triangulo(lado1, lado2, lado3):
        s = (lado1 + lado2 + lado3) / 2
        area = math.sqrt(s * (s - lado1)*(s - lado2)*(s - lado3))
        return round(area, 4)
    else:
        return "No se puede calcular el área"

datos_prueba = [
    [3, 4, 5],      # Triángulo 1: Triángulo rectángulo clásico (3-4-5)
    [5, 5, 6],      # Triángulo 2: Triángulo isósceles
    [7, 7, 7],      # Triángulo 3: Triángulo equilátero
    [10, 12, 16],   # Triángulo 4: Triángulo escaleno
    [2, 2, 8],      # Triángulo 5: NO ES UN TRIÁNGULO (caso de error)
]

resultados_esperados = [
    6.0,
    12.0,
    21.2176,
    59.9249,
    0.0 # Asumiendo que la función devuelve 0 o maneja el error si no es un triángulo
]

for i in range(len(datos_prueba)):
    if calcular_area(datos_prueba[i][0], datos_prueba[i][1], datos_prueba[i][2]) == resultados_esperados[i]:
        print("Correcto")
    else:
        print("Error")
    
print(calcular_area(7, 7, 7))
print(calcular_area(10, 12, 16))
