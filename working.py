import re

def main():
    print(convert(input("Hours: ")))

def convert(hours):

    pattern = r'(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)'

    match = re.fullmatch(pattern, hours)

    if not match:
        raise ValueError("Invalid Format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start_minute = start_minute if start_minute else '00'

    end_minute = end_minute if end_minute else '00'

    start_time_24 = convert_to_24(start_hour, start_minute, start_period)
    end_time_24 = convert_to_24(end_hour, end_minute, end_period)

    return f"{start_time_24} to {end_time_24}"

def convert_to_24(hour, minute, period):
    hour = int(hour)
    minute = int(minute)

    if period == "AM":
        if hour == 12:
            hour = 0

    elif period == "PM":
        if hour != 12:
            hour += 12

    if not(0 <= hour <= 23 and 0 <= minute <= 59)


