from datetime import date

def main():
    birthday = birthdate()

    birthday1, birthday2  = birthday.split(",") #they have to be in words, with no and

    print(f"{birthday1}{birthday2} minutes
{birthday1} moments so dear
{birthday1}{birthday2}
How do you measure, measure a year?")

def birthdate(birthday):

    date_birthday = (input("What's your birthday? Use YYYY-MM-DD "))

    time_of_birth = date(date_birthday)

