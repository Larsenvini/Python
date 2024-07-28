def main():
    plate = input("Vanity Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):

    if not (2 <= len(plate) <= 6):
        return False

    if not plate[:2].isalpha():
        return False

    if not plate.isalnum():
        return False

    number_started = False
    for char in plate:
        if char.isdigit():
            if char == '0' and not number_started:
                return False
            number_started = True
        elif number_started:
            return False

    return True

main()

