def main():

    greeting = input("Greet your client ").strip().lower()
    print(greet(greeting))


def greet(msg):
    if msg.startswith("hello", "Hello", "HELLO"):
        return "$0"

    elif msg.startswith("h", "H"):
        return "$20"

    else:
        return "$100"

if __name__ == "__main__":
    main()
