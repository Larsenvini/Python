the_answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip()

match the_answer:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")


