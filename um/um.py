import re
import sys

def main():
    print(count(input("Text: ")))

def count(sentence):
    pattern = re.search(r'[ um ]', sentence, re.IGNORECASE)

