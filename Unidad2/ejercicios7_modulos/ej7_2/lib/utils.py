#!/usr/bin/env python3

'''Módulo utils.py con registro de invocaciones externas.'''

# Esta inicialización ocurre solo una vez cuando se importa el módulo
_invocations_counter = 0

def suma(lista):
    '''Devuelve la suma de los valores y registra la invocación si es externa.'''
    global _invocations_counter
    
    # Si el módulo no es el programa principal, contamos la invocación
    if __name__ != "__main__":
        _invocations_counter += 1
    
    total = 0
    for x in lista:
        try:
            total += x
        except TypeError:
            print(f"Error: {x} no es numérico.")
    return total

def producto(lista):
    '''Devuelve el producto de los valores y registra la invocación si es externa.'''
    global _invocations_counter
    
    if __name__ != "__main__":
        _invocations_counter += 1
        
    if not lista: return 0
    total = 1
    for x in lista:
        try:
            total *= x
        except TypeError:
            print(f"Error: {x} no es numérico.")
    return total

def get_counter():
    '''Función auxiliar para consultar el contador desde fuera.'''
    return _invocations_counter

# Pruebas internas
if __name__ == "__main__":
    print("--- Pruebas internas de utils.py ---")
    # Aquí el contador no debería aumentar según la lógica solicitada
    print(f"Suma: {suma([1, 2, 3])}")
    print(f"Contador (debe ser 0 en pruebas): {_invocations_counter}")