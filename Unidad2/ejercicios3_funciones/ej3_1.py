## AÑO BISIESTO

def es_bisiesto(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    
test_data = [1900, 2000, 2016, 1987] 
test_results = [False, True, True, False] 

for i in range(len(test_data)):
    if es_bisiesto(test_data[i]) != test_results[i]:
        print("ERROR")
    else:
        print("CORRECTO")


