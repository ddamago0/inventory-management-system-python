# Function to add a product to the inventory

from validate_inventory import validate_inventory

def add_product(inventory):

    product = validate_inventory()
    inventory.append(product)

    print("Product added successfully.")