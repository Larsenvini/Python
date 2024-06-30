def main():
    while True:
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
        except (ValueError, ZeroDivisionError):
            continue


def convert_to_percentage(prompt):
    x, y = prompt.split("/")

    x = int(x)

    y = int(y)

    if x > y:
        raise ZeroDIvisionError

    if y == 0:
        raise ValueError

    percentage = (x / y) * 100

    return round(percentage)


main()
