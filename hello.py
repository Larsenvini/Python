def main():
    name = input("What's your name? ").lower().capitalize()
    hello(name)

def hello(to = "World"):
     print("Hello,", to)

if __name__ == "__main__":
     main()

