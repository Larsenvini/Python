giria = input("Input: ")
vogals = {"a" : "",
           "e" : "",
             "i": "",
               "o" : "",
                 "u" : "",
                 "O" : ""}

vog = giria.maketrans(vogals)

giria = giria.translate(vog)
print (giria)


