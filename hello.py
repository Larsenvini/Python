def main():
    name = input("What's your name? ").lower().capitalize()
    print(hello(name))


def hello(to = "World"):
     return f"Hello, {to}"

if __name__ == "__main__":
     main()

