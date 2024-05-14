def main():
    meal = input("What time is it? ")
    convert(meal)
    meal_definer(meal)
    print(meal)




def meal_definer(food):
    if 7 <= food > 8:
        print("breakfast")
    elif 12 <= food > 13:
        print("lunch")
    elif 18 <= food > 19:
        print("dinner")
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



main()


if __name__ == "__main__":
    main()
