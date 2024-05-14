def main():
    meal = input("What time is it? ")
    convert(meal)


#:## a.m. and ##:## a.m.
#:## p.m. and ##:## p.m.


def convert(time):
    hours, minutes = time.split(":")
    

main()


if __name__ == "__main__":
    main()
