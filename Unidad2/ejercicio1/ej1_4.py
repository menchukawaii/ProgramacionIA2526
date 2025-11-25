year = int (input("Introduce el año"))

if year < 1582:
    print("Fuera del período del calendario gregoriano")
elif year %4 != 0:
    print("Año común")
else:
    print("Año bisiesto")
