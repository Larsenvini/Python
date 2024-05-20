def main():
    convert = input(": ")
    converted = add_(convert)
    print (converted)

def add_(arroba):
    "".join('_' + i if i.isupper() else i for i in arroba)
    arroba.lower()
    return arroba

main()









