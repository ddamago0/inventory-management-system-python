# Function to display all products in the inventory

def show_inventory(inventory):

    # Check if inventory is empty
    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    # Loop through the inventory
    for product in inventory:

        print(
            f"Product: {product['name']} | "
            f"Price: {product['price']} | "
            f"Quantity: {product['quantity']}"
        )