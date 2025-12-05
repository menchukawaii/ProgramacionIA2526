'''
===========================REGISTRO TEMPERATURAS===========================

El servicio de meteorología incorpora en el registro de temperaturas de la
ciudad, la temperatura media de cada semana, el día más cálido y el día más
frío, y una alerta si hubo algún día con una amplitud térmica (diferencia entre
las temperaturas máxima y mínima) superior a 15 grados.

Se dispone de un diccionario donde, para cada día de la semana
(“lunes”, “martes”, ..) se recogen las temperaturas mínima y máxima alcanzadas.

Recomendaciones: antes de iniciar el análisis de los datos, comprueba que los
datos contenidos en el diccionario son correctos (la temperatura mínima es
menor o igual a la temperatura máxima).
Utiliza funciones para cada parte del análisis.
'''

temperaturas_semanales_lista = {
    "lunes": [12.5, 23.0],
    "martes": [14.0, 25.5],
    "miercoles": [13.2, 24.8],
    "jueves": [15.1, 16.3],
    "viernes": [16.0, 28.1],
    "sabado": [17.5, 30.5],
    "domingo": [10.9, 27.2]
}

def comprobacion_temperaturas(temperaturas_semanales_lista):
    for key, value in temperaturas_semanales_lista.items():
        if value[1] < value[0]:
            return f"Las temperaturas del {key} son incorrectas"
    return True

def add_media(temperaturas_semanales_lista):
    for key, value in temperaturas_semanales_lista.items():
        media = (value[0] + value[1]) / 2
        value.append(media)


def add_amplitud_termica(temperaturas_semanales_lista):
    for key, value in temperaturas_semanales_lista.items():
        if value[1] - value[0] >= 15:
            value.append(True)
        else:
            value.append(False)



def actualizar_registro_temperaturas(temperaturas_semanales_lista):
    resultado_comprobacion = comprobacion_temperaturas(temperaturas_semanales_lista)
    if resultado_comprobacion is True:
       add_media(temperaturas_semanales_lista)
       add_amplitud_termica(temperaturas_semanales_lista)
       return temperaturas_semanales_lista
    else:
        return resultado_comprobacion


print(actualizar_registro_temperaturas(temperaturas_semanales_lista))




    
