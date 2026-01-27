def calcular_precio(articulo, cantidad, lista_productos):
    articulo_encontrado = None
    for i in lista_productos:
        if i["nombre"] == articulo:
            articulo_encontrado = i
    if not articulo_encontrado: raise ValueError("El articulo no existe")
    precio_total = articulo_encontrado["precio"] * int(cantidad)
    return precio_total