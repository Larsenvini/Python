giria = input("Input: ")
vogals = {"a" : "",
           "e" : "",
             "i": "",
               "o" : "",
                 "u" : ""}
vog = giria.maketrans(vogals)

giria = giria.translate(vogals)
print (giria)


