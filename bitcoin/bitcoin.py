import requests
import sys

def main():
    while True:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            converted_response = response * sys.argv[1]




            print(f"${converted_response:,.4f}")
        except requests.RequestException:
            sys.exit()
    ...
if __name__ == "__main__":
    main()
