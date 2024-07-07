def main():
    plate = input("Vanity Plate: ")
    if is_valid(plate):
        print("Valid")
        return 0  # Returning 0 to indicate success
    else:
        print("Invalid")
        return 1  # Returning non-zero to indicate failure

def is_valid(s):
    if len(s) != 6:
        return False

    half_length = len(s) // 2
    part1 = s[:half_length]
    part2 = s[half_length:]

    if not part1.isalpha() or len(part1) != 2:
        return False

    if not part2.isdigit() or len(part2) != 2:
        return False

    if '0' in part2:
        return False

    return True

if __name__ == "__main__":
    import sys
    sys.exit(main())
