def main():
    yell("opa bebe vamo ali")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

main()
