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
    if hours == 7 and minutes > 0 | minutes < 60:
        return float(hours, minutes)

main()


if __name__ == "__main__":
    main()
