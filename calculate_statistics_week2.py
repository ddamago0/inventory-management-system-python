# Function to calculate inventory statistics

def calculate_statistics(inventory):

    # Check if inventory is empty
    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    # Accumulators
    total_value = 0
    total_products = 0

    # Loop through inventory
    for product in inventory:

        total_value += product["price"] * product["quantity"]
        total_products += product["quantity"]

    # Show results
    print(f"Total inventory value: {total_value}")
    print(f"Total number of products: {total_products}")