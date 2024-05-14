def main():
    greeting = input("Greet your client ").strip().lower()


    match greeting:
        case "hello":
            print("$0")

        case "hey" | "hi" | "hey there":
            print("$20")

        case _:
            print("$100")

main()
