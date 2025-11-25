"""Mejora el programa anterior. Escribe un programa que use: 
 un bucle for. 
 el concepto de ejecución condicional (if-elif-else). 
 la instrucción conƟnue.
Tu programa debe: 
 pedir al usuario que ingrese una palabra. 
 uƟlizar user_word = user_word.upper() para converƟr la palabra ingresada por el usuario a 
mayúsculas 
 emplea la ejecución condicional y la instrucción conƟnue para "devorar" las siguientes vocales 
A , E , I , O , U de la palabra ingresada. 
 asigna las letras no consumidas a la variable word_without_vowels e imprime la variable en la 
pantalla.  """

palabra = input("Ingresa una palabra")
palabra = palabra.upper()
vocales = "AEIOU"
resultado = ""
word_without_vowels = ""
for i in palabra:
    if i in vocales:
        word_without_vowels += i
        continue
    resultado += i
print(f"Resultado: {resultado}")
print(f"Vocales eliminadas: {word_without_vowels}")
