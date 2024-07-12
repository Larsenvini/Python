import re

def main():
    print(count(input("Text: ")))



def count(sentence):

    if sentence != str:
        raise ValueError("Invalid format")

    pattern = re.compile(r'\bum\b', re.IGNORECASE)

    matches = re.findall(pattern, sentence)

    return len(matches)

if __name__ == '__main__':
    main()
