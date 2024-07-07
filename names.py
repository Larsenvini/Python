names = []

for _ in range(3):
    names.append(input("Whats your name? ").capitalize())

for name in sorted(names):
    print(f"Hello, {name}")
