import requests
import sys
def main():
    opa("weezer")
def opa():
    if len(sys.argv) != 2:
        sys.exit()

response = requests.get("https://itunes.apple.com/search/?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
