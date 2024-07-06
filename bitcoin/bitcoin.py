import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error: Unable to retrieve data from the API.")

    data = response.json()

    try:

        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
    except KeyError:
        sys.exit("Error: Unexpected response format.")


    total_cost = num_bitcoins * price_per_bitcoin

    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()

