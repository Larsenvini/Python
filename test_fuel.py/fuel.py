def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(prompt):
    x, y = prompt.split("/")

    x = int(x)

    y = int(y)

    if x > y:
        raise ZeroDivisionError

    if y == 0:
        raise ValueError

    return x, y

def gauge(percentage):
    percentage = (x / y) * 100

    return round(percentage)



if __name__ == "__main__":
    main()
