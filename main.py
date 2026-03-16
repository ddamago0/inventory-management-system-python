from validate_inventory import validate_inventory
from calculate_total import calculate_total
from show_result import show_result

# Main function that controls the program

def main():

    product = validate_inventory()
    total = calculate_total(product)
    show_result(product, total)

if __name__ == "__main__":
    main()