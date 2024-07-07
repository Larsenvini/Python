def main():
    plate = input("Vanity Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
     if len(s) != 6:
        return False
     half_lenght = len(s) // 2

     part1 = s[:half_lenght]
     part2 = s[half_lenght:]

     if not part1.isalpha() or len(part1) != 2:
        return False

     if not part2.isdigit() or len(part2) != 2:
        return False

     if '0' in part2:
         return False

if __name__ == "__main__":
    main()
