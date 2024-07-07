vogals = {"a" : "",
           "e" : "",
             "i": "",
               "o" : "",
                 "u" : "",
                 "O" : ""}


def main():
    giria = input("Input: ")
    print (giria)


def shorten(giria):

    vog = giria.maketrans(vogals)

    giria = giria.translate(vog)


if __name__ == "__main__":
    main()
