import re

url = input("Whats your twitter username? ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/.+$", url, re.IGNORECASE)

if matches:
    print(f"Username: ", matches.group(2))
