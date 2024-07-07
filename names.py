names = input("Whats your name? ")

file = open("names.txt", "w")
file.write(names)
file.close()
