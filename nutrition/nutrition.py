fruit = input("Input: ")
calories = {"Apple" : "130",
           "Avocado California" : "50",
             "Banana": "110",
               "Cantaloupe " : "50",
                 "Grapefruit" : "60",
                 "Grapes" : "90",
                 "Honeydew Melon": "50",
                 "Kiwifruit":"90",
                 "Lemon":"15",
                 "Lime":"20",
                 "Nectarine":"60",
                 "Orange ":"80",
                 "Peach":"60",
                 "Pear":"100",
                 "Pineapple":"50",
                 "Plums":"70",
                 "Strawberries":"50",
                 "Sweet Cherries":"100",
                 "Tangerine":"50",
                 "Watermelon":"80",
                 }

# Create a translation table for fruit names to their respective calorie counts
translation_table = str.maketrans(calories)

fruit = input("Input a fruit name: ")

# Use the translation table with the translate method
calories_count = fruit.translate(translation_table)

print(calories_count)

