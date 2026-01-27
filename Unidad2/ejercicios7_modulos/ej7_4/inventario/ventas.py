def vender(articulo, cantidad, lista_productos):
    articulo_encontrado = None
    for i in lista_productos:
        if i["nombre"] == articulo:
            articulo_encontrado = i
    if not articulo_encontrado: raise ValueError("El articulo no existe")
    articulo_encontrado["cantidad_disponible"] -= int(cantidad)
    return articulo_encontrado["cantidad_disponible"]
