import re

name = input("What's your name? ").strip()

matches = re.search(r"ˆ.+, ?.+$", name)
