'''
==============================ENCUESTA==============================

Tu tarea es escribir un programa que, a partir de una serie de pares de valores
(nombre, edad) ingresados por el usuario, genere un diccionario
(la key será el nombre) y lo muestre por pantalla.

Implementa una función para leer los datos:
recibirá el nombre y la edad, y seguirá recibiendo datos mientras el nombre
ingresado sea diferente de 0. (Se supone que cuando el usuario ya no va
a incluir más pares nombre, edad escribirá un 0

Diseña una función que imprima la edad y nombre de las personas
mayor y menor respectivamente. Para facilitar la solución, puedes suponer
que no hay edades repetidas.
'''

def leer_diccionario(diccionario):


def oldest(diccionario):



def youngest(diccionario):


def cargar_usuarios():
    diccionario = {}
    while True:
        nombre = input("Ingrese el nombre (o '0' para finalizar): ")
        if nombre == '0':
            break
        else:
            edad_str = input(f"Ingrese la edad de {nombre}: ")
            edad = int(edad_str) 
            diccionario[nombre] = edad
            print(f"'{nombre}': {edad} añadido.")
    return diccionario:

def leer_diccionario(diccionario):
    """
    Lee pares (nombre, edad) del usuario y los añade al diccionario.
    La lectura termina cuando el nombre ingresado es '0'.
    """
    print("\n--- INGRESO DE DATOS ---")
    while True:
        nombre = input("Ingrese el nombre (o '0' para finalizar): ")
        if nombre == '0':
            break  # Termina el bucle si se ingresa '0'
        
        try:
            # Pide la edad y la convierte a entero
            edad_str = input(f"Ingrese la edad de {nombre}: ")
            edad = int(edad_str)
            
            # Añade el par al diccionario
            diccionario[nombre] = edad
            print(f"'{nombre}': {edad} añadido.")
        except ValueError:
            # Maneja el caso en que la edad no sea un número válido
            print("**Error**: La edad debe ser un número entero. Inténtelo de nuevo.")
            
    return diccionario

def oldest(diccionario):
    """
    Encuentra e imprime el nombre y la edad de la persona de mayor edad.
    Se asume que el diccionario no está vacío y no hay edades repetidas.
    """
    if not diccionario:
        print("\nEl diccionario está vacío. No hay persona mayor.")
        return
        
    # Usamos la función max() con una función lambda como 'key' para buscar 
    # el elemento con el valor (edad) más alto.
    # .items() devuelve pares (key, value), y el max() lo compara por el value[1] (la edad).
    nombre_mayor, edad_mayor = max(diccionario.items(), key=lambda item: item[1])
    
    print(f"\n👵 Persona de **MAYOR** edad:")
    print(f"- **Nombre**: {nombre_mayor}")
    print(f"- **Edad**: {edad_mayor}")

def youngest(diccionario):
    """
    Encuentra e imprime el nombre y la edad de la persona de menor edad.
    Se asume que el diccionario no está vacío y no hay edades repetidas.
    """
    if not diccionario:
        print("\nEl diccionario está vacío. No hay persona menor.")
        return

    # Usamos la función min() con una función lambda como 'key' para buscar 
    # el elemento con el valor (edad) más bajo.
    nombre_menor, edad_menor = min(diccionario.items(), key=lambda item: item[1])
    
    print(f"\n👶 Persona de **MENOR** edad:")
    print(f"- **Nombre**: {nombre_menor}")
    print(f"- **Edad**: {edad_menor}")

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # Inicializa el diccionario vacío
    encuesta_diccionario = {}
    
    # 1. Llamar a la función para leer los datos y llenar el diccionario
    encuesta_diccionario = leer_diccionario(encuesta_diccionario)

    # 2. Mostrar el diccionario resultante
    print("\n--- DICCIONARIO FINAL ---")
    if encuesta_diccionario:
        # sorted() ordena las claves (nombres) para una mejor presentación
        for nombre, edad in sorted(encuesta_diccionario.items()):
            print(f"{nombre}: {edad} años")
    else:
        print("El diccionario está vacío.")

    # 3. Llamar a las funciones para encontrar el mayor y el menor
    if encuesta_diccionario:
        print("\n" + "="*30)
        oldest(encuesta_diccionario)
        print("-" * 30)
        youngest(encuesta_diccionario)
        print("="*30)
