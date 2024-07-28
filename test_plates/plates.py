def main():
    plate = input("Enter your vanity plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the length is between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if the plate starts with letters
    if not s[:2].isalpha():
        return False

    # Check if all characters are alphanumeric
    if not s.isalnum():
        return False

    # Check if numbers, if present, are at the end and do not start with zero
    # Find the first occurrence of a digit
    first_digit_index = len(s)  # Default to length of string if no digits found
    for i, char in enumerate(s):
        if char.isdigit():
            first_digit_index = i
            break

    # If there are digits in the plate, check their placement
    if first_digit_index < len(s):
        if first_digit_index == len(s) - 1:  # Only one digit (invalid case)
            return False
        if s[first_digit_index] == '0':  # Leading zero
            return False
        if not s[first_digit_index:].isdigit():  # Non-digit characters after digits
            return False

    return True


def starts_with_letters(s):
    # Check if the first two characters are letters
    return len(s) >= 2 and s[0].isalpha() and s[1].isalpha()

def has_correct_length(s):
    # Check if the length is between 2 and 6 characters
    return 2 <= len(s) <= 6

def numbers_at_end(s):
    # Check if numbers, if present, are at the end and the first number is not zero
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not number_started:
                # If the first digit is zero, return False
                if char == '0':
                    return False
                number_started = True
        elif number_started:
            # If a letter appears after numbers started, return False
            return False
    return True

def contains_only_allowed_characters(s):
    # Check if the plate contains only alphanumeric characters
    return s.isalnum()

if __name__ == "__main__":
    main()
