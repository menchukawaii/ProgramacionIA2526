'''
===========================RESTAURANTE===========================
Tu tarea es calcular la calificación media de los platos del menú de un
restaurante. Las valoraciones de los clientes se recogen en un diccionario
que contiene como claves los nombres de los platos, y como valor una lista
de tuplas con el nombre del cliente y la calificación dada (de 1 a 5).

Ordenar los platos del menú del restaurante por su calificación media,
de mayor a menor. Recomendación: puedes crear un nuevo diccionario con
las puntuaciones medias y ordenarlo. La función sorted() devuelve una
lista ordenada con los elementos del iterable que se le pasa como parámetro.
Un segundo argumento de la función es el parámetro key, que permite
especificar el campo por el que se ordenará (diccionario.get devuelve
los valores del diccionario). Un tercer argumento de la función es el
parámetro reverse, que toma el valor True/False si se quiere ordenar en
orden inverso.

Aumenta la funcionalidad de tu programa generando un informe con los platos
que tienen una calificación menor a 3, indicando el número de veces que fueron
calificados con menos de 3.

Implementa una función que permita al cliente agregar una calificación.
'''
valoraciones_clientes = {
    "Macarrones a la carbonara": [
            ("Carmen", 5),
            ("Pablo", 1),
            ("Nerea", 4),
            ("Aleix", 1)
        ],
    "Tortilla de patata": [
            ("Carmen", 1),
            ("Pablo", 1),
            ("Nerea", 4),
            ("Aleix", 1)
        ],
    "Sopa": [
            ("Carmen", 2),
            ("Pablo", 3),
            ("Nerea", 4),
            ("Aleix", 1)
        ]    
}

def calcular_media_plato(valoraciones_clientes):
    nota_media = {}
    for key, value in valoraciones_clientes.items():
        media_plato = 0
        for valoracion in value:
            media_plato += valoracion[1]
        media_plato = media_plato / len(value)
        nota_media[key] = media_plato
    return nota_media

print(f"Nota media: {calcular_media_plato(valoraciones_clientes)}")


def ordenar_por_media(valoraciones_clientes):
    nota_media = calcular_media_plato(valoraciones_clientes)
    ordenada = sorted(
        nota_media.items(), 
        key=lambda item: item[1], 
        reverse=True
    )
    return ordenada
        
        

print(ordenar_por_media(valoraciones_clientes))

def platos_baja_calificacion(valoraciones_clientes):
    informe = {}
    medias = calcular_media_plato(valoraciones_clientes)
    for plato, valoraciones in valoraciones_clientes.items():
        print(medias.get(plato, 0))
        if medias.get(plato, 0) < 3:
            conteo_bajas = 0
            for nombre, nota in valoraciones:
                if nota < 3:
                    conteo_bajas += 1
            informe[plato] = {
                "media": medias[plato],
                "veces_menos_de_3": conteo_bajas
            }
    return informe


print(platos_baja_calificacion(valoraciones_clientes))



def agregar_calificacion(valoraciones_clientes, plato, cliente, nota):
    if plato in valoraciones_clientes:
        valoraciones_clientes[plato].append((cliente, nota))
    else:
        valoraciones_clientes[plato] = [(cliente, nota)]
    return valoraciones_clientes


print(agregar_calificacion(valoraciones_clientes, "Macarrones a la carbonara", "Paula", 5))
