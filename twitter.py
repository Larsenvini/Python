import re

url = input("Whats your twitter username? ").strip()

username = re.sub(r"^https?:)?(wwww\.)?//twitter\.com/", "", url)

print(username)


