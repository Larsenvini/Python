giria = input("Input: ")
vogals = {"a" : "",
           "e" : "",
             "i": "",
               "o" : "",
                 "u" : ""}
vog = giria.maketrans(vogals)

giria = giria.translate(vog)
print (giria)


