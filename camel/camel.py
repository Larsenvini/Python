def main():
    convert = input(": ") #get input
    converted = add_(convert) #transform uppercase in lower and add _ before originally uppercased letters
    print (converted)#print the converted string

def add_(arroba):
    return "".join('_' + i if i.isupper() else i for i in arroba).lower()


main()``









