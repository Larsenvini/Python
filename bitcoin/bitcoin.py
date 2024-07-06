import requests
import sys

def get_amount(response):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json" + sys.argv[1])
    return response

def convert(response):
    while True:
        try:
         converted_response = response.float 

        except requests.RequestException:
            sys.exit()
    ...

def main():
    while True:
        try:



            print(response.json())
        except requests.RequestException:
            sys.exit()
    ...
