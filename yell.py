def main():
    yell("opa bebe vamo ali")

def yell(*words):
    """
    before:
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
        after:
        """
    uppercased = map(str.upper, words)
    print(*uppercased)

main()
