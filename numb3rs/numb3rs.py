import re
import sys

def main():
    ipv4 = sys.argv[1]
    print(validate(ipv4))


def validate(ip):

    ns = r'[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-1][0-9]|22[0-5]'

    if re.search(fr'^(?:{ns}\.{ns}\.{ns}\.{ns})$'):
        return "Valid"
    else:
        return "Invalid"

if __name__ == '__main__':
    main()
