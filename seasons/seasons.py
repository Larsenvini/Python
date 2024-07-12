from datetime import date

def main():
    birthday = birthdate()

    birthday1, birthday2  = birthday.split(",") #they have to be in words, with no and

    print(f"{birthday1}{birthday2} minutes\n{birthday1} moments so dear\n{birthday1}{birthday2}\nHow do you measure, measure a year?")

def birthdate():

    date_birth = (input("What's your date of birth? Use YYYY-MM-DD "))# getting the birth date

    year, month, day = date_birth.split("-")

    d = date(year, month, day)

    diff_minutes = year_to_minutes(d)

    return diff_minutes

def year_to_minutes(years):
    today = date.today()


    difference_in_days = (today - years).days

    minutes = difference_in_days * 24 * 60

    return minutes

if __name__ == "__main__":
    main()
