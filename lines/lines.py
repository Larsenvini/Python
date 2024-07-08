import os
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <filename.py>")


    filename = sys.argv[1]

    if not filename.endwith(".py"):
        sys.exit("File must end with .py")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with open(filename, "r") as file:
            lines = file.readlines(filename)
    except Exception as e:
        sys.exit("Error:{e}")

    code_lines = count_code_lines(lines)
    print(code_lines)

def count_code_lines(lines):
    for line in lines:
        empty_line = line.strip()
        if empty_line and not empty_line.startswith("#"):
            
