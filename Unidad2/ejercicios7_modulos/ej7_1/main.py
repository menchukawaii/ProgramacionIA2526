import basics

def ejecutar():
    print("Iniciando programa principal...")
    
    try:
        # Uso de factorial
        num = 6
        res_fact = basics.factorial(num)
        print(f"El factorial de {num} es: {res_fact}")

        # Uso de hipotenusa
        lado1, lado2 = 5, 12
        res_hipo = basics.hipotenusa(lado1, lado2)
        print(f"La hipotenusa de {lado1} y {lado2} es: {res_hipo}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    ejecutar()