def meow(n: int):
    for _ in range(n):
        return n * "meow\n"

number: int = int(input("Number? "))
meows: str = meow(number)
print(meows)
