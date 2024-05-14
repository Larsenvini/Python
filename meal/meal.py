def main():
    meal = input("What time is it? ")
    converted_time = convert(meal)

    if 7 <= converted_time and converted_time <= 8:
        print("breakfast time")

    elif 12 <= converted_time and converted_time <= 13:
            print("lunch time")
    elif 18 <= converted_time and converted_time <= 19:
            print("dinner time")
    else:
            print(" ")







#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    decimal_minutes = minutes / 60

    converted_time = hours + decimal_minutes

    return converted_time






if __name__ == "__main__":
    main()
