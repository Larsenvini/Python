import os
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <filename.py>")


    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a python file")

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
    code_lines = 0
    for line in lines:
        empty_line = line.strip()
        if not empty_line and line.startswith("#"):
            code_lines += 1

    return code_lines

if __name__ == "__main__":
    main()
