def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert_to_percentage(fraction)
        if percentage <= 1:
            print("E")
            elif percentage 


def get_fraction(prompt):
    while True:
        try:
            return (input(prompt))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
