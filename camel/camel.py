def main():
    convert = input(": ").lower()
    converted = add_(convert)
    print (converted)

def add_(arroba):
    "".join('_' + i if i.isupper() else i for i in arroba)
    return arroba

main()









