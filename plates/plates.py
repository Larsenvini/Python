def main():
    plate = input("Vanity Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Not Valid")

def is_valid(algo):
    if algo.startswith(int):
        
