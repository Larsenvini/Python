import re

email = input("What's your email? ").strip()

if re.search(r'^\ww+@(\2+\.)?\2+\.edu$', email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
