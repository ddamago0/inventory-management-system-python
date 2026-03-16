# Funtion to calculate the total cost of the product

def calculate_total(product):

    # Multiply price by quantity
    total = product["price"] * product["quantity"]

    # Return the calculated total
    return total