def main():
    convert = input(": ")
    add_(convert)
    print (convert.lower())

def add_(s):
    s.join('_' + i if i.isupper() else i for i in s)

main()









