import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def get_date():
    while True:
        date_st = input().strip()

        match = re.match(r'^(\d{1,2})/(\d{1,2})/(\d{4})$', date_str)

        if match:
            month, day, year = match.groups()
            try:
                return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
            except ValueError:
                pass

        match = re.match(r'^(\w+) (\d{1,2}), (\d{4})$', date_str)

        if match:
            month_str, day, year = match.groups()
            try:
                return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
            except ValueError:
                pass
