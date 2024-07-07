names = (input("Whats your name? ").capitalize())

with open("names.txt", "a") as file:
    file.write(f"{names}\n")

