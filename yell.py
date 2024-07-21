def main():
    yell("opa bebe vamo ali")

def yell(*words):
    """
    before:
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    after: using map

    uppercased = map(str.upper, words)
    print(*uppercased)
    """
    uppercased = [word.upper() for word in words]
    print(*uppercased)
main()
