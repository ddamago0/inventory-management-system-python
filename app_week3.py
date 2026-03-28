from servicios_week3 import *
from archivos_week3 import guardar_csv
from archivos_week3 import cargar_csv
#Validate float
def input_float(mensaje):
    f = True
    while f:
        try:
            valor = float(input(mensaje))

            if valor <= 0:
                print ("Error: value must be positive.")
            else:
                return valor
        
        except ValueError:
            print ("Error: Please enter a valid number.")
            

#Validate int
def input_int(mensaje):
    i = True
    while i:
        try:
            valor = int(input(mensaje))

            if valor <= 0:
                print("Error: value must be positive.")
            else:
                return valor

        except ValueError:
            print("Error: please enter a valid integer.")

#Validate str
def input_string(mensaje):
    s = False
    while not s:
        valor = input(mensaje).strip()

        if valor == "":
            print("Error: cannot be empty.")

        elif not valor.replace(" ","").isalpha():
            print ("Error: product name cannot contain numbers or symbols.")
        
        else:
            s = True
            return valor
        

def app():
    inventario = []
    running = True

    while running:
        print("\n--- MENU ---")
        print("1. Add product")
        print("2. Show inventory")
        print("3. Search product")
        print("4. Update product")
        print("5. Delete product")
        print("6. Statistics")
        print("7. Save CSV")
        print("8. Load CSV")
        print("9. Exit")

        opcion = input ("Select an option: ")


        #Opcion 1
        if opcion == "1":
            nombre = input_string("Enter the product name: ")
            precio =  input_float("Enter the price: ")
            cantidad = input_int("Enter the quantity: ")

            agregar_producto(inventario, nombre, precio, cantidad)
            print ("Saved product.")

        #Opcion 2
        elif opcion == "2":
            mostrar_inventario(inventario)

        #Opcion 3
        elif opcion == "3":
            nombre = input_string("Name to search: ")
            producto = buscar_producto(inventario, nombre)

            if producto:
                print (producto)

            else:
                print ("Product not found.")

        #Opcion 4
        elif opcion == "4":
            nombre = input_string ("Name to update: ")
            precio = input_float("New price: ")
            cantidad = input_int("New quantity: ")

            actualizado = actualizar_producto(inventario, nombre, precio, cantidad)

            if actualizado:
                print ("Updated product.")

            else:
                print ("Product not found.")

        #Opcion 5
        elif opcion == "5":
            nombre = input_string("Name to delete: ")

            eliminado = eliminar_producto (inventario, nombre)

            if eliminado:
                print("Product removed.")
            else:
                print("Product not found.")

        #Opcion 6
        elif opcion == "6":
            stats = calcular_estadisticas(inventario)

            if stats:
                print (f"Total units: {stats['unidades_totales']}")
                print (f"Total value: {stats['valor_total']:.2f}")
                print (f"Most expensive product: {stats['producto_mas_caro']['nombre']}")
                print (f"Greater stock: {stats['producto_mayor_stock']['nombre']}")

            else:
                print ("empty inventory.")


        #Opcion 7
        elif opcion == "7":
            ruta = input("Enter file path (Example: inventario.csv): ")
            guardar_csv(inventario, ruta)


        #Opcion 8
        elif opcion == "8":
            ruta = input("Enter file path: ")
            nuevo_inventario = cargar_csv(ruta)

            if not nuevo_inventario:
                print ("No valid data loaded.")
                continue

            decision = input("Overwrite inventory? (S/N): ").lower()

            if decision == "s":
                inventario = nuevo_inventario
                print("Inventory replaced.")

            elif decision == "n":
                for nuevo in nuevo_inventario:
                    existente = buscar_producto(inventario, nuevo["nombre"])
                    if existente:
                        # Sumar cantidad
                        existente["cantidad"] += nuevo["cantidad"]

                        # actualizar precio
                        existente["precio"] = nuevo["precio"]

                    else:
                        inventario.append(nuevo)

                print ("Inventory merged.")

            else:
                print ("Invalid option.")
        
        #Opcion 9
        elif opcion == "9":
            print ("leaving...")
            running = False

        else:
            print ("Invalid option.")

if __name__ == "__main__":
    app()