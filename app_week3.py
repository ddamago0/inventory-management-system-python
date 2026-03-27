from servicios_week3 import *

def app():
    inventario = []
    running = True

    while running:
        print("\n--- MENU ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        opcion = input ("Seleccione una opcion: ")

        #Opcion 1
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            precio = float (input("Ingrese el precio: "))
            cantidad = int (input("Ingrese la cantidad"))

            agregar_producto(inventario, nombre, precio, cantidad)
            print ("Producto agregado.")

        #Opcion 2
        elif opcion == "2":
            mostrar_inventario(inventario)

        #Opcion 3
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            producto = buscar_producto(inventario, nombre)

            if producto:
                print (producto)

            else:
                print ("Producto no encontrado.")

        #Opcion 4
        elif opcion == "4":
            nombre = input ("Nombre a actualizar: ")
            precio = float (input("Nuevo precio: "))
            cantidad = int (input("Nueva cantidad: "))

            actualizado = actualizar_producto(inventario, nombre, precio, cantidad)

            if actualizado:
                print ("Producto actualizado.")

            else:
                print ("Producto no encontrado.")

        #Opcion 5
        elif opcion == "5":
            nombre = input("Nombre a eliminar: ")

            eliminado = eliminar_producto (inventario, nombre)

            if eliminado:
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        #Opcion 6
        elif opcion == "6":
            stats = calcular_estadisticas(inventario)

            if stats:
                print (f"Total unidades: {stats['unidades_totales']}")
                print (f"Valor total: {stats['valor_total']}")
                print (f"Producto mas caro: {stats['producto_mas_caro']['nombre']}")
                print (f"Mayor stock: {stats['producto_mayor_stock']['nombre']}")

            else:
                print ("Inventario vacio.")

        
        #Opcion 9
        elif opcion == "9":
            print ("Saliendo...")
            running = False

        else:
            print ("Opcion invalida.")

if __name__ == "__main__":
    app()