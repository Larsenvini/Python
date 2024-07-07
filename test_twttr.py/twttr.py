vogals = {"a" : "",
           "e" : "",
             "i": "",
               "o" : "",
                 "u" : "",
                 "O" : ""}


def main():
    nome = input("Input: ")
    nome_feito = shorten(nome)
    output = print(nome_feito)
    print (output)


def shorten(giria):

    vog = giria.maketrans(vogals)

    giria = giria.translate(vog)

    return giria


if __name__ == "__main__":
    main()
