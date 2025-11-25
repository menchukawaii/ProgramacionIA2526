## FACTORIAL DE UN NÚMERO (n)

def factorial(num):
    factorial = 1
    if num == 0 or num == 1:
        return 1
    elif num > 0:
        for i in range(num, 0, -1):
            factorial *= i
    else:
        return "No se puede calcular"
    return factorial


def factorial_recursivo(num):
    if num == 0 or num == 1:
        return 1

    elif num > 0:
        return num * factorial_recursivo(num - 1)

    else:
        return "No se puede calcular"

datos_prueba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultados_esperados = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

for i in range(len(datos_prueba)):
    if factorial_recursivo(datos_prueba[i]) == resultados_esperados[i]:
        print("Correcto")
    else:
        print("Error")
