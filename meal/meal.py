def main():
    meal = input("What time is it? ")
    convert(meal)
    if 7 <= (meal) > 8:
        print("breakfast")



#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.


def convert(time):
    hours, minutes = time.split(":")
    if hours == 7 and minutes > 0 | minutes < 60:
        return float()

main()


if __name__ == "__main__":
    main()
