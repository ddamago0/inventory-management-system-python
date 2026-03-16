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