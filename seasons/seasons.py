from datetime import date

def main():
    birthday = birthdate()

    birthday1, birthday2  = birthday.split(",") #they have to be in words, with no and

    print(f"{birthday1}{birthday2} minutes\n{birthday1} moments so dear\n{birthday1}{birthday2}\nHow do you measure, measure a year?")

def birthdate():

    date_birthday = (input("What's your birthday? Use YYYY-MM-DD "))

    year, month, day = date_birthday.split("-")

    d = date(year, month, day)

    minutes = year_to_minutes(d)

    return minutes

def
if __name__ == "__main__":
    main()
