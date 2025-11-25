ingreso = float(input("Intruce el ingreso"))
impuesto = 0
if ingreso <= 85528:
    impuesto = ingreso * 0.18 - 556.2
else:
    impuesto = 14839.2 + ((ingreso - 85528) * 0.32)

if impuesto < 0:
    impuesto = 0

print(f"El impuesto es {round(impuesto, 0)}€")
