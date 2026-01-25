import sys
import os

# Obtenemos la ruta absoluta del directorio donde está main.py
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Construimos la ruta a la carpeta 'lib'
ruta_lib = os.path.join(directorio_actual, 'lib')

# La añadimos al path si no está ya ahí
if ruta_lib not in sys.path:
    sys.path.append(ruta_lib)

# Ahora la importación no debería fallar
import basics
import utils

def main():
    numeros = [2, 4, 6]
    
    print("=== Resultados de BASICS ===")
    print(f"Factorial de 4: {basics.factorial(4)}")
    
    print("\n=== Resultados de UTILS (desde subcarpeta lib) ===")
    print(f"La suma de {numeros} es: {utils.suma(numeros)}")
    print(f"El producto de {numeros} es: {utils.producto(numeros)}")

    # Prueba de error en utils
    print("\nPrueba de robustez en utils con lista mixta:")
    lista_mixta = [10, "hola", 20]
    print(f"Suma de {lista_mixta}: {utils.suma(lista_mixta)}")

if __name__ == "__main__":
    main()