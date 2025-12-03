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

def leer_diccionario():
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
    return diccionario

def oldest(diccionario):
    edad_mayor = 0
    nombre_mayor = ""
    for clave, valor in diccionario.items():
        if edad_mayor < valor:
            edad_mayor = valor
            nombre_mayor = clave
    return f"{nombre_mayor} {diccionario[nombre_mayor]}"


def youngest(diccionario):
    edad_menor = 150
    nombre_menor = ""
    for clave, valor in diccionario.items():
        if edad_menor > valor:
            edad_menor = valor
            nombre_menor = clave
    return f"{nombre_menor} {diccionario[nombre_menor]}"


'''
-----------------------CASOS DE PRUEBA-----------------------
'''
diccionario = leer_diccionario()
print(diccionario)
print(f"El mayor es: {oldest(diccionario)}")
print(f"El menor es: {youngest(diccionario)}")
