import re

url = input("Whats your twitter username? ").strip()

re.search(r"^https?://(www\.)?twitter\.com/.+$", url, re.IGNORECASE)
