import inflect

p = inflect.engine()

def main():
    names = []

    try:
        while True:
            name = input("Name: ").strip()
            if name:
                names.append(name)
    except EOFError:
            pass

    formatted_names = p.join(names)

    print(f"Adieu, adieu, to {formatted_names}")

if __name__ == "__main__":
    main()
