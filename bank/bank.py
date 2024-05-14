def main():
    greeting = input("Greet your client ").strip().lower()


    match greeting:
        case "Hello":
            print("$0")

        case find("h"):
            print("$20")

        case _:
            print("$100")

def find(n):
    n = str.find("h")

main()
