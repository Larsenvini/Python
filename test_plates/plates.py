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
    if not numbers_at_end(s):
        return False
    if contains_only_allowed_characters(s):
        return True
    return False

def starts_with_letters(s):
    # Check if the string starts with at least two letters
    return s[:2].isalpha()

def has_correct_length(s):
    # Check if the string has a length between 2 and 6 characters
    return 2 <= len(s) <= 6

def numbers_at_end(s):
    # Check if numbers are only at the end of the string
    if s[-1].isdigit():
        return True
    return False

def contains_only_allowed_characters(s):
    # Check if the string contains only uppercase letters and digits
    return s.isalnum() and s.isupper()

if __name__ == "__main__":
    main()
