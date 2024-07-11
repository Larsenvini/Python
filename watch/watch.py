import re
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python watch.py <html.address>")
    html = sys.argv[1]
    print(parse(html))

def parse(s):

    html = r^("[http](s)?://(www.)?youtube.com/embed/\w"$)

    if re.search(html, s):




...


if __name__ == "__main__":
    main()
