def main():
    meal = input("What time is it? ")
    convert(meal)
    print(meal)



#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    decimal_minutes = minutes / 60

    converted_time = hours + decimal_minutes

    return converted_time



main()


if __name__ == "__main__":
    main()
