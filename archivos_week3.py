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


def cargar_csv(ruta):
    """
    Loads inventory from a CSV file.

    Returns:
    list of products
    """

    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:

            lineas = archivo.readlines()

            # Validar header
            header = lineas[0].strip()
            if header != "nombre,precio,cantidad":
                print("Error: invalid file format.")
                return []

            # Leer datos
            for linea in lineas[1:]:

                partes = linea.strip().split(",")

                if len(partes) != 3:
                    errores += 1
                    continue

                nombre, precio, cantidad = partes

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    producto = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }

                    inventario.append(producto)

                except ValueError:
                    errores += 1

        print(f"Loaded products: {len(inventario)}")
        print(f"Invalid rows: {errores}")

        return inventario

    except FileNotFoundError:
        print("Error: file not found.")
        return []

    except UnicodeDecodeError:
        print("Error: invalid file encoding.")
        return []

    except Exception as e:
        print(f"Unexpected error: {e}")
        return []