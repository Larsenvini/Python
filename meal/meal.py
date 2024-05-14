def main():
    meal = input("What time is it? ")

    hours, minutes = meal.split(":")


    convert(meal)
    if 7 <= meal > 8:
        print("breakfast")



#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.


def convert(time):
    if 7 <= time > 8:
        return float(time)


main()


if __name__ == "__main__":
    main()
