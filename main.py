# Import function from week 1
from validate_inventory import validate_inventory
from show_inventory import show_inventory
from calculate_statistics import calculate_statistics
from add_product import add_product

# Main function that controls the program
def main():


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
            add_product(inventory)

        # Option 2: Show inventory
        elif option == "2":
            show_inventory(inventory)

        # Option 3: Statistics
        elif option == "3":
            calculate_statistics(inventory)

        # Option 4: Exit
        elif option == "4":
            print("Exiting program...")
            running = False

        # Invalid option
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()