prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}

def main():
    total = 0.0  # Initialize total to keep track of the sum of prices

    while True:
        try:
            order = input("Item: ").strip().title()  # Use .title() to match the keys' format

            if order in prices:
                total += prices[order]  # Add the item's price to the total
                print(f"Total: ${total:.2f}")  # Print the running total
            else:
                raise ValueError  # Raise ValueError if the item is not found in prices

        except ValueError:
            pass  # If a ValueError is raised, continue the loop and prompt again

main()
