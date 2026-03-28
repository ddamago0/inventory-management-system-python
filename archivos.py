def guardar_csv(inventario, ruta, incluir_header = True):
    """
    Saves the inventory to a CSV file.

    paremeters:
    inventario (list): list of products
    ruta (str): file path
    incluir_header (bool): include header row
    """

    if len(inventario) == 0:
        print ("Error: inventory is empty.")
        return
    
    try:
        with open(ruta, "w", encoding = "utf-8") as archivo:
            # Header
            if incluir_header:
                archivo.write("nombre,precio,cantidad\n")

            # Data
            for producto in inventario:
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)

        print(f"Inventory saved in: {ruta}")

    except PermissionError:
        print("Error: permission denied.")

    except Exception as e:
        print(f"Unexpected error: {e}")