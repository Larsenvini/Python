import requests
import sys

def main():
    while True:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            converted_response = response * sys.argv[1]




            print(converted_response)
        except requests.RequestException:
            sys.exit()
    ...
if __name__ == "__main__":
    main()
