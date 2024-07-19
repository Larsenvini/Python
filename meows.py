def meow(n: int):
    for _ in range(n):
        return n * "meow\n"

"""

Meow n times

:param n: Number of times to meow

:type n: int

:raise TypeError: If n is not an int

:return: A string of n meows, one per line

:rtype: str

"""

number: int = int(input("Number? "))
meows: str = meow(number)
print(meows, end="")
