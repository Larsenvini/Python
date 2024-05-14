def main():
    meal = input("What time is it? ")
    convert(meal)
    if 7 <= meal > 8:
        print("breakfast")



#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.


def convert(time):
    hours, minutes = time.split(":")
    return float(time)


main()


if __name__ == "__main__":
    main()
