from random import randint
n = randint(0,100)
n_user = int(input("Ingresa un numero del 0 al 100"))
while n_user != n:
    if n_user < n:
        print("Mas alto")
    else:
        print("Mas bajo")
    n_user = int(input("Ingresa un numero del 0 al 100"))
print(f"Enhorabuena! El numero es {n}")
