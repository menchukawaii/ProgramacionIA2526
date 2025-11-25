"""La sentencia conƟnue se usa para omiƟr el bloque actual y avanzar a la siguiente iteración, sin ejecutar 
las sentencias dentro del bucle. Se puede usar tanto con bucles while y for. 
Escribe un programa que use: 
un bucle for; 
el concepto de ejecución condicional (if-elif-else). 
la sentencia conƟnue.
Tu programa debe ser un Devorador de vocales (bastante feo) con los siguientes pasos: 
 pedir al usuario que ingrese una palabra. 
 Utliza user_word = user_word.upper() para converƟr la palabra ingresada por el usuario a 
mayúsculas; 
 Utliza la ejecución condicional y la instrucción conƟnue para "devorar" las vocales de la 
palabra ingresada. 
 Imprime las letras restantes en la pantalla, en una misma línea  """

palabra = input("Ingresa una palabra")
palabra = palabra.upper()
vocales = "AEIOU"
resultado = ""
for i in palabra:
    if i in vocales:
        continue
    resultado += i
print(resultado)
