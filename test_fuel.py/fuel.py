def main():
    while True:
        fraction = input("Fraction: ")

        percentage = convert(fraction)

        print(gauge(percentage))



def convert(prompt):
    x, y = prompt.split("/")

    x = int(x)

    y = int(y)

    if x > y:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    percentage = (x / y) * 100

    return round(percentage)

def gauge(percentage):
    while True:
          try:
             if percentage <= 1:
                print("E")
             elif percentage >= 99:
                print("F")
             else:
                print(f"{percentage}%")
                break

          except (ValueError, ZeroDivisionError):
              continue

if __name__ == "__main__":
    main()
