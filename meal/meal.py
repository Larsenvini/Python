def main():
    meal = input("What time is it? ").strip(":")

    convert(meal)
    if 7 <= meal > 8:
        print("breakfast")



#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.


def convert(time):

    return float(time)


main()


if __name__ == "__main__":
    main()
