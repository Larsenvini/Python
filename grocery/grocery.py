grocery_list = {}

while True:
    try:
        item = input().strip().lower()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        break

