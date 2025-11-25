from random import *

FILAS = 31
COLUMNAS = 24

matriz = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

temperatura_mediodia = 0
temperatura_mas_alta = 15
dias_a_20_grados = 0

for i in range(FILAS):
    for j in range(COLUMNAS):
        matriz[i][j] = round(uniform(15, 40), 1)
        #temperatura mediodia
        if j == 12:
            temperatura_mediodia += matriz[i][j]
            #contador de dias con temperatura al menos de 20º a mediodia
            if matriz[i][j] >= 20:
                dias_a_20_grados += 1
        #temperatura mas alta
        if matriz[i][j] > temperatura_mas_alta:
            temperatura_mas_alta = matriz[i][j]


temperatura_mediodia = temperatura_mediodia/31

for fila in matriz:
    print(fila)

print(f"temperatura mediodia {temperatura_mediodia}")
print(f"temperatura mas alta {temperatura_mas_alta}")
print(f"dias con al menos 20º a mediodia: {dias_a_20_grados}")
