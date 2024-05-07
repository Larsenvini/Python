def main():
    name = str.lower(input("Whats is your favorite food and computer science course? "))
    first, last = name.split
    hello(name)

def hello(para):
    print("Nice!", first, "Is a great food.", "And", last, "is a great course!!")

main()
