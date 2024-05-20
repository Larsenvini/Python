def main():
    convert = input(": ").lower()
    add_(convert)
    print (convert)

def add_(s):
    s.join('_' + i if i.isupper() else i for i in s)









