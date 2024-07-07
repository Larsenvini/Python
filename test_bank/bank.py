def main():

    greeting = input("Greet your client ").strip().lower()
    print(value(greeting))


def value(msg):
    if msg.startswith("hello"):
        return "$0"

    elif msg.startswith("h"):
        return "$20"

    else:
        return "$100"

if __name__ == "__main__":
    main()
