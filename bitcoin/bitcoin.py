import requests
import sys

def convert():
    

def main():
    while True:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json" + sys.argv[1])

            print(response.json())
        except requests.RequestException:
            sys.exit()
    ...
