# Inventory service functions

def agregar_producto(inventario,nombre,precio,cantidad):
    """
    adds a new product to the inventory
    
    parameters:
    inventario (list): list of de products
    nombre (str): product name
    precio (float): product price
    cantidad (int): product quantity
    """

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

def mostrar_inventario(inventario):
    """
    Displays all products in the inventory
    """
    if len(inventario) == 0:
        print ("Inventory is empty")
        return
    
    for producto in inventario:
        print (f"Producto: {producto['nombre']} | Precio: {producto['precio']: .2f} | Cantidad: {producto['cantidad']}")

def buscar_producto (inventario, nombre):
    """
    Searches for a product by name.

    returns:
    dict or none
    """

    for producto in inventario:
        if producto ["nombre"].lower() == nombre.lower():
            return producto
    
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Updates a product's price and/or quantity.
    """

    producto = buscar_producto(inventario,nombre)

    if producto is None:
        return False

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    return True

def eliminar_producto (inventario, nombre):
    """
    Deletes a product from the inventory.
    """

    producto = buscar_producto(inventario, nombre)

    if producto is None:
        return False
    inventario.remove(producto)
    return True

def calcular_estadisticas(inventario):
    """
    Calculates inventory statistics.

    Returns:
    dict with statistics
    """

    if len(inventario) == 0:
        return None
    
    unidades_totales = 0
    valor_total = 0

    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    for producto in inventario:
        unidades_totales += producto["cantidad"]
        valor_total += producto["precio"] * producto["cantidad"]

        if producto ["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        if producto ["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }