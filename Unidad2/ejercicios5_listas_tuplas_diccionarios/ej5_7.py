'''
===========================INVENTARIO===========================
En una empresa se lleva el inventario de productos de sus tiendas mediante
un diccionario, en el que cada producto está representado como una clave en
el diccionario y el valor es una lista de tuplas donde cada tupla contiene el
precio de venta, la cantidad disponible, y la cantidad mínima de stock.

Tu tarea consiste en:

• Calcular el valor total del inventario de cada producto
    (precio * cantidad).

• Añadir un cálculo para el valor total del inventario
    (suma del valor de todos los productos).
    
• Crear una función para agregar productos nuevos al inventario con la
    estructura adecuada.

• Realizar control de existencias: generar un informe con los productos
    que tienen menos de la cantidad mínima en stock.

'''

#precio de venta, cantidad disponible, y cantidad mínima de stock
inventario_tiendas = {
    "Laptop ProX": [
        (1200.50, 5, 2),  # Tienda A: Precio, Disponible, Mínimo
        (1210.00, 10, 3), # Tienda B
        (1199.99, 1, 1)   # Tienda C
    ],
    "Ratón Ergonómico Z": [
        (25.99, 50, 10),
        (26.50, 45, 15)
    ],
    "Monitor UltraHD 27": [
        (350.00, 8, 4),
        (349.50, 20, 5),
        (355.00, 2, 3)
    ],
    "Teclado Mecánico K1": [
        (75.00, 15, 5)
    ],
    "Disco SSD 1TB": [
        (89.99, 0, 5),   # Producto agotado en esta tienda (0 disponible)
        (92.00, 12, 8)
    ]
}


def calcular_valor_inventario_por_producto(inventario_tiendas):
    valor_inventario = {}
    for key, valor in inventario_tiendas.items():
        valores = []
        for tienda in valor:
            valores.append(tienda[0] * tienda[1])
        valor_inventario[key] = valores  
    return valor_inventario

print(f"Calcular el valor total del inventario de cada producto:\n {calcular_valor_inventario_por_producto(inventario_tiendas)}")
print("\n===============================================\n")

def calcular_valor_total_inventario(inventario_tiendas):
    valor_por_producto = calcular_valor_inventario_por_producto(inventario_tiendas)
    valor_total = 0 
    for key, value in valor_por_producto.items():
        for valor_por_tienda in value:
            valor_total += valor_por_tienda
    return round(valor_total, 2)

print(f"Añadir un cálculo para el valor total del inventario:\n {calcular_valor_total_inventario(inventario_tiendas)}")
print("\n===============================================\n")

def agregar_productos(productos, inventario_tiendas):
    for key, value in productos.items():
        if key in inventario_tiendas:
            for i in value:
                inventario_tiendas[key].append(i)
        else:
            inventario_tiendas[key] = value
    return inventario_tiendas

productos = {
    "Laptop ProX" :[
        (89.99, 5, 5)
        ],
    "Movil 2" :[
        (150, 25, 5),
        (150, 50, 5)
        ],
    "Movil 3" :[
        (500, 50, 5)
        ]
    }
inventario_tiendas = agregar_productos(productos, inventario_tiendas)
print("Crear una función para agregar productos nuevos al inventario con la estructura adecuada\n")
print(inventario_tiendas)
print("\n===============================================\n")

def control_existencias(inventario_tiendas):
    informe = []
    for key, value in inventario_tiendas.items():
        print(key)
        for tienda in value:
            print(tienda)
            if tienda[2] >= tienda[1]:
                informe.append(key)
    return informe
print("Realizar control de existencias: generar un informe con los productos que tienen menos de la cantidad mínima en stock\n")
print(control_existencias(inventario_tiendas))
print("\n===============================================\n")
















