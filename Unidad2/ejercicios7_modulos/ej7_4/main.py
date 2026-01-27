from inventario.productos import lista_productos
from inventario.ventas import vender
from inventario.utilidades import calcular_precio

def realizar_venta(lista_productos):
    nombre = input("Introduce el nombre del articulo")
    cantidad = input("Introduce la cantidad a comprar")
    try:
        precio = calcular_precio(nombre, cantidad, lista_productos)
        print(f"El precio total es de {precio:.2f}€")
        stock = vender(nombre, cantidad, lista_productos)
        print(f"Despues de la venta quedan {stock} unidades de {nombre}")
    except ValueError as e:
        print(f"Error : {e}")

realizar_venta(lista_productos)