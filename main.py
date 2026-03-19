# Import function from week 1
from validate_inventory import validate_inventory

# Create empty inventory list
inventory = []

# Control variable for the loop
running = True

# Main menu loop
while running:

    print("\n--- INVENTORY MENU ---")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Exit")

    option = input("Choose an option: ")

    # Option 1: Add product
    if option == "1":
        print("Add product option")

    # Option 2: Show inventory
    elif option == "2":
        print("Show inventory option")

    # Option 3: Statistics
    elif option == "3":
        print("Calculate statistics option")

    # Option 4: Exit
    elif option == "4":
        print("Exiting program...")
        running = False

    # Invalid option
    else:
        print("Invalid option. Try again.")