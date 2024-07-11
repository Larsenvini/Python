import re

def main():
    print(convert(input("Hours: ")))

def convert(hours):

    pattern = r'(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)'

    match = re.fullmatch(pattern, hours)

    if not match:
        raise ValueError("Invalid Format")
