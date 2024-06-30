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
        while True:
            try:
                order = input("Item: ").lower()

                if order in (key.lower() for key in prices):
                    prices_count = prices[next(key for key in prices if key.lower() == order)]
                    print(f"Total: {prices_count}")
                elif order not in prices:
                     raise ValueError
                else:
                     break

            except ValueError:
                pass
main()
