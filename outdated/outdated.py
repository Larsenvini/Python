import re

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def get_date():
    while True:
        date_str = input().strip()

        # Try to match numerical month format (e.g., 9/8/1636)
        match = re.match(r'^(\d{1,2})/(\d{1,2})/(\d{4})$', date_str)
        if match:
            month, day, year = match.groups()
            try:
                month, day, year = int(month), int(day), int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:  # Validate month and day ranges
                    return f"{year:04d}-{month:02d}-{day:02d}"
            except ValueError:
                pass  # If conversion fails, prompt again

        # Try to match textual month format (e.g., September 8, 1636)
        match = re.match(r'^(\w+) (\d{1,2}), (\d{4})$', date_str)
        if match:
            month_str, day, year = match.groups()
            if month_str in months:
                try:
                    month = months.index(month_str) + 1
                    day, year = int(day), int(year)
                    if 1 <= day <= 31:  # Validate day range
                        return f"{year:04d}-{month:02d}-{day:02d}"
                except ValueError:
                    pass  # If conversion fails, prompt again

if __name__ == "__main__":
    valid_date = get_date()
    print(valid_date)

