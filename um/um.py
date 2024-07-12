import re
import sys

def main():
    print(count(input("Text: ")))

def count(sentence):

    pattern = re.compile(r'\bum\b', re.IGNORECASE)

    matches = re.findall(pattern, sentence)

    return len(matches)

main()
