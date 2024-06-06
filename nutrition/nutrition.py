
calories = { "Apple" : "130",
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
             "Watermelon":"80" }

fruit = input("Input a fruit name: ").lower()

if fruit in (key.lower() for key in calories):  # Convert dictionary keys to lower case for comparison
    calories_count = calories[next(key for key in calories if key.lower() == fruit)]
    print(calories_count)  # Print title case for the fruit name
else:
    print("")

