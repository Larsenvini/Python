with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())
