import inflect
from datetime import date, datetime

def main():
    birthdate = get_birthdate()
    birthday1, birthday2 = birthdate.split(",", 1)

    print(f"{birthdate}\n{birthday1} moments so dear\n{birthdate} minutes\nHow do you measure, measure a year?")

def get_birthdate(date_birth=None):
          if not date_birth:
                date_birth = input("What's your date of birth? Use YYYY-MM-DD ")
          birth_date = datetime.strptime(date_birth, "%Y-%m-%d").date()

          today = date.today()
          delta = today - birth_date

          minutes = delta.days * 24 * 60


          minutes_in_words = number_to_words(minutes)
          return minutes_in_words

def number_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="").replace("-", " ")

    words = words.replace("-", " ")
    words = words.capitalize()

    return words

if __name__ == "__main__":
    main()
