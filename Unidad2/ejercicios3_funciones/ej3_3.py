##numero de dia
def es_bisiesto(year):
    if year < 1582:
        return "No se puede calcular, no está en el calendario gregoriano."
    else:
        if year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False

def dias_del_mes(year, month):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month -= 1 ##para que el mes se adapte al indice del array
    ##if month <=12 and month >=1
    if month in range(len(dias_mes)):
        if month == 2 and es_bisiesto(year):
            return 29
        else:
            return dias_mes[month]
    else:
        return "El mes es incorrecto"

def numero_dia(year, month, day):
    if day in range(32):
        dias = 0
        for i in range(1, month):
            dias += dias_del_mes(year, i)
        dias += day
        return dias
    else:
        return "dia incorrecto"

print(dias_del_mes(1500,12))
print(numero_dia(2000, 12, 31))
print(numero_dia(2000, 2, 30))

