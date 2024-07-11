import re
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python watch.py <html.address>")
    html = sys.argv[1]
    print(parse(html))

def parse(s):
    



...


if __name__ == "__main__":
    main()
