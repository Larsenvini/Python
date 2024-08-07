import inflect
from datetime import date, datetime
import sys

def main():
    birthdate = get_birthdate()

    print(f"{birthdate} minutes")

def get_birthdate(date_birth=None):
          if not date_birth:
                date_birth = input("What's your date of birth? Use YYYY-MM-DD ")
          try:
            birth_date = datetime.strptime(date_birth, "%Y-%m-%d").date()

          except ValueError:
               sys.exit(1)


          today = date.today()
          delta = today - birth_date

          minutes = delta.days * 24 * 60


          minutes_in_words = number_to_words(minutes)
          return minutes_in_words

def number_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="", wantlist=False)

    return words.capitalize()

if __name__ == "__main__":
    main()
