def main():
    name = str.lower(input("Please type in your favorite food and computer science course, separated by a blank space. (example: banana cs50) "))
    name = name.strip(",")
    hello(name)

def hello(para):
    first, last = para.split(" ")
    print("Nice!", first, "is a great food.", "And", last, "is a great course!!")

main()
