import inflect

p = inflect.engine()

def main():
    names = []

    while True:
        try:
            name = input("Name: ").strip()
            if name:
                names.append(name)
        except EOFError:
            pass

    formatted_names = p.join(names)
