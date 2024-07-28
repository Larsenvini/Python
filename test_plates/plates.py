def main():
    plate = input("Enter your vanity plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not starts_with_letters(s):
        return False
    if not has_correct_length(s):
        return False
    if not contains_only_allowed_characters(s):
        return False
    if not numbers_at_end(s):
        return False
    return True

def starts_with_letters(s):
    # Check if the first two characters are letters
    return s[:2].isalpha()

def has_correct_length(s):
    # Check if the length is between 2 and 6 characters
    return 2 <= len(s) <= 6

def numbers_at_end(s):
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0' and not number_started:
                return False
            number_started = True
        elif number_started:
            return False
    return True

def contains_only_allowed_characters(s):
    return s.isalnum()

if __name__ == "__main__":
    main()
