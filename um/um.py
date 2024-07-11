import re
import sys

def main():
    print(count(input("Text: ")))

def count(sentence):

    um_count = 0

    pattern = re.search(r'[ um ]', sentence, re.IGNORECASE)

    if pattern in sentence:
        for pattern in sentence:
            um_count += 1

    return um_count


