def main():
    plate = input("Vanity Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(algo):
    half_lenght = len(algo) // 2
    alg1 = algo[:half_lenght]
    alg2 = algo[half_lenght:]
    if alg1.isalpha():

        if len(alg1) == 2:
            return True
        else:
            return False
    if alg2.isdigit():
        if len(alg2) == 2:
            return True
        else:
            return False

if __name__ == "__main__":
    main()
