def main():
    convert = input(": ").lower()
    add_(convert)
    print (convert)

def add_(s):
    s.join('_' + s if s.isupper())









