def gestion_inventario(accion, inventario, producto=None, cantidad=0):
    if accion == "agregar":
        if producto in inventario:
            inventario[producto] += cantidad
            print("Cantidad actualizada")
        else:
            inventario[producto] = cantidad
            print( f"Producto {producto} agregado. Cantidad total: {inventario[producto]}")
    elif accion == "eliminar":
        if producto in inventario:
            if inventario[producto] >= cantidad:
                inventario[producto] -= cantidad
                if inventario[producto] == 0:
                    del inventario[producto]
                print( f"Producto {producto} eliminado. Cantidad restante: {inventario.get(producto, 0)}")
            else:
                print( "Cantidad a eliminar excede la cantidad en inventario.")
        else:
            print( "Producto no encontrado en inventario.")
    elif accion == "buscar":
        if producto in inventario:
            print( f"Producto {producto} encontrado. Cantidad: {inventario[producto]}")
        else:
            print( "Producto no encontrado en inventario.")
    else:
        print( "Acción no válida. Use 'agregar', 'eliminar' o 'buscar'.")

inventario = {"ordenador" : 1,
              "movil": 35,
              "tablet": 3}
prueba = [["agregar", inventario, "ordenador", 15], ["agregar", inventario, "ordenador", 15]]
resultado = [["Cantidad actualizada", ]

for i in range(len(prueba)):

    if gestion_inventario(accion, inventario, producto, cantidad) == resultados[i]:
        print("CORRECTO")
    else:
        print()



