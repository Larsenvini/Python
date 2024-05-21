giria = input("Input: ")
vogals = giria.maketrans()
vogals = {"a" : "",
           "e" : "",
             "i": "",
               "o" : "",
                 "u" : ""}
giria = giria.translate(vogals)
print (giria)


