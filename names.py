names = (input("Whats your name? "))

file = open("names.txt", "a")
file.write(names)
file.close()
