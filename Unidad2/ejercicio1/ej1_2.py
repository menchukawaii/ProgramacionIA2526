
try:
    millas = float(input("Introduce las millas"))
    km = float(input("Introduce los km"))
    print(f"{millas} millas son {millas*1.61} millas" )
    print(f"{km} km son {km/1.61} millas" )

except ValueError:
    print("No se peude introducir texto")
except:
    print("Entrada no valida")
    
    

