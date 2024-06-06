fruit = input("Input: ")
calories = {"Apple" : "130",
           "Avocado California" : "50",
             "Banana": "110",
               "Cantaloupe " : "50",
                 "Grapefruit" : "60",
                 "Grapes" : "90",
                 "Honeydew Melon": "50",
                 "Kiwifruit":"90",
                 "":"",
                 }

per_fruit = fruit.maketrans(calories)

fruit = fruit.translate(per_fruit)
print (fruit)
