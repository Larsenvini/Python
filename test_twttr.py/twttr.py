vogals = {"a" : "",
           "e" : "",
             "i": "",
               "o" : "",
                 "u" : "",
                 "O" : ""}


def main():
    nome = input("Input: ")
    print(shorten(nome))



def shorten(giria):

    vog = giria.maketrans(vogals)

    giria = giria.translate(vog)

    return giria


if __name__ == "__main__":
    main()
