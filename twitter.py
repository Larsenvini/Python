import re

url = input("Whats your twitter username? ").strip()

username = re.sub(r"https://twitter.com/", "", url)

print(username)


