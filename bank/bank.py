def main():
    greeting = input("Greet your client ").strip().lower()


    match greeting:
        case "Hello":
            print("$0")

        case "Hey" | "Hi" | "Hey there":
            print("$20")

        case _:
            print("$100")

main()
