from datetime import date, datetime

def main():
    birthdate = get_birthdate()
    minutes = calculate_age_in_minutes(birthdate)

    print(f"{minutes})

if __name__ == "__main__":
    main()
