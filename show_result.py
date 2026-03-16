# Function to display the product information and total cost

def show_result(product, total):

    print ("\n----- Product Summary -----")

    print (
        f"Product: {product['name']} | "
        f"Price: {product['price']} | "
        f"Quantity: {product['quantity']} | "
        f"Total: {total}"

    )