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
    except:
        raise()

