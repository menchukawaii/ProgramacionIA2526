"""La instrucción break se implementa para salir/terminar un bucle. 
Diseña un programa que use un bucle while y le pida conƟnuamente al usuario que ingrese una palabra 
a menos que ingrese "chupacabra" como la palabra de output secreta, en cuyo caso el mensaje "Has 
dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar. 
No imprimas ninguna de las palabras ingresadas por el usuario. UƟliza el concepto de ejecución 
condicional y la sentencia break.  """

palabra = input("Ingresa una palabra")
while True :
    if palabra == "chupacabra":
        print("Has salido del bucle")
        break
    palabra = input("Ingresa una palabra")
