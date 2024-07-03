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
                
