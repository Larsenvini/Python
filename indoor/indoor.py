def main():
    name = str.lower(input("Whats is your favorite food and computer science course? ")).strip(",")
    hello(name)

def hello(para):
    first, last = para.split(" ")
    print("Nice!", first, "Is a great food.", "And", last, "is a great course!!")

main()
