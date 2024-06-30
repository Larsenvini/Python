prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.0  # Initialize total to keep track of the sum of prices

    while True:
        try:
            order = input("Item: ").strip().title()  # Use .title() to match the keys' format

            if order in prices:
                total += prices[order]  # Add the item's price to the total
                print(f"Total: ${total:.2f}")  # Print the running total
            else:
                print("Invalid item. Please enter a valid item from the menu.")  # Inform user of invalid input

        except EOFError:
            print()  # Print a newline when EOF is encountered
            break  # Exit the loop when EOF is encountered

main()
