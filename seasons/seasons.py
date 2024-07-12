import inflect
from datetime import date, datetime

def main():
    birthdate = get_birthdate()
    birthday1, birthday2 = birthdate.split(",", 1)

    print(f"{birthdate}\n{birthday1} moments so dear\n{birthdate} minutes\nHow do you measure, measure a year?)

def get_birthdate():
          date_birth = input()

if __name__ == "__main__":
    main()
