def main():
    convert = input(": ")
    converted = add_(convert)
    print (converted)

def add_(s):
    "".join('_' + i if i.isupper() else i for i in s)
    s.lower()

main()









