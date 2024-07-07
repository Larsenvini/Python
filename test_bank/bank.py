def main():

    greeting = input("Greet your client ").strip().lower()
    
    if greeting.startswith("hello"):
        print("$0")

    elif greeting.startswith("h"):
        print("$20")

    else:
        print("$100")

main()
