# This function asks the user for product information
# and validates the data entered

def validate_inventory():

#--------Validate product name -----------
    valid_name = False

    while not valid_name :
        name = input("Enter the product name: ").strip()

        if name == "":
            print("Enter: Product name cannot be empty.")

        elif not name.repleace(" ","").isalpha():
            print ("Error: Product name cannot contain numbers or symbols.")

        else:
            valid_name = True

#------ Validate product price --------

valid_price = False

while not valid_price:
    try:
        price = float (input("Enter the product price: "))

        if price <= 0:
            print ("Error: Price must be greater than 0.")

        else:
            valid_price = True

    except ValueError:
        print ("Error: Please enter a valid number.")