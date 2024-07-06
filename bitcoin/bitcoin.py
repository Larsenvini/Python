import requests
import sys

if len(sys.argv) != float:
    sys.exit()

response = requests.get("https://itunes.apple.com/search/?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())

def main()
    while True:
        try:
    ...
        except requests.RequestException:
    ...
