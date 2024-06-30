def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert_to_percentage(fraction)
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
            break
    except(ValueError, ZeroDivisionError):
        continue


def get_fraction(prompt):
    while True:
        try:
            return (input(prompt))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
