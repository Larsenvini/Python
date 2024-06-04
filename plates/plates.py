def main():
    plate = input("Vanity Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Not Valid")

def is_valid(algo):
    alg1, alg2 = algo.partition(2)
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

main()
