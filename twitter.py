import re

url = input("Whats your twitter username? ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/.([a-z0-9_]+))$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))
