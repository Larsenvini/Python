from datetime import date

def main():
    birthday = birthdate()

    birthday1, birthday2  = birthday.split(",") #they have to be in words, with no and

    print(f"{birthday1}{birthday2} minutes\n{birthday1} moments so dear\n{birthday1}{birthday2}\nHow do you measure, measure a year?")

def birthdate():

    date_birthday = (input("What's your birthday? Use YYYY-MM-DD "))

    time_of_birth = date(date_birthday)

    minutes = time_of_birth.minutes

    return minutes

if __name__ == "__main__":
    main()
