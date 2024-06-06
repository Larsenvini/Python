fruit = input("Input: ")
calories = {"a" : "",
           "e" : "",
             "i": "",
               "o" : "",
                 "u" : "",
                 "O" : ""}

per_fruit = fruit.maketrans(calories)

fruit = fruit.translate(per_fruit)
print (fruit)
