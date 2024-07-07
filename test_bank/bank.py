def main():

    greeting = input("Greet your client ").strip()
    print(f"${value(greeting)}")


def value(msg):
    if not isinstance(msg, str):
        raise TypeError("Input must be a string")

    msg = msg.lower()

    if msg.startswith("hello"):
        return 0

    elif msg.startswith("h"):
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()
