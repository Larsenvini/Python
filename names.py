names = (input("Whats your name? ").capitalize())

file = open("names.txt", "a")
file.write(f"{names}\n")
file.close()
