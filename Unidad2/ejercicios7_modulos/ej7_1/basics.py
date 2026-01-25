import math

def factorial(n):
    #Calcula el factorial de un número entero no negativo n.
    if not isinstance(n, int):
        raise TypeError("El valor debe ser un número entero.")
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo.")
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def hipotenusa(a, b):
    #Calcula la hipotenusa de un triángulo rectángulo dados sus catetos a y b.
    try:
        # La fórmula es: c = sqrt(a^2 + b^2)
        return (a**2 + b**2)**0.5
    except TypeError:
        raise TypeError("Los lados deben ser valores numéricos.")

# Bloque de validación (solo se ejecuta si corres este archivo directamente)
if __name__ == "__main__":
    print("--- Ejecutando pruebas unitarias en basics.py ---")
    
    # Prueba de Factorial
    test_n = 5
    mi_fact = factorial(test_n)
    math_fact = math.factorial(test_n)
    print(f"Factorial de {test_n}: Propio={mi_fact} | Math={math_fact}")
    assert mi_fact == math_fact, "Error en la función factorial"

    # Prueba de Hipotenusa
    cat_a, cat_b = 3, 4
    mi_hipo = hipotenusa(cat_a, cat_b)
    math_hipo = math.hypot(cat_a, cat_b)
    print(f"Hipotenusa ({cat_a}, {cat_b}): Propia={mi_hipo} | Math={math_hipo}")
    assert mi_hipo == math_hipo, "Error en la función hipotenusa"

    print("--- Todas las pruebas pasaron con éxito ---")