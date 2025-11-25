##dia del mes

def es_bisiesto(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def dias_del_mes(year, month): 
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and es_bisiesto(year):
        return 29
    else:
        return dias_mes[month - 1]

 
test_years = [1900, 2000, 2016, 1987] 
test_months = [2, 2, 1, 11] 
test_results = [28, 29, 31, 30] 


for i in range(len(test_results)):
    if dias_del_mes(test_years[i], test_months[i]) != test_results[i]:
        print("ERROR")
    else:
        print("CORRECTO")
