import re
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python numb3rs.py <ipv4.address>")
    ipv4 = sys.argv[1]
    print(validate(ipv4))


def validate(ip):

    ns = r'(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'

    pattern = fr'^{ns}\.{ns}\.{ns}\.{ns}$'

    if re.search(pattern, ip):
        return True
    else:
        return False

if __name__ == '__main__':
    main()
