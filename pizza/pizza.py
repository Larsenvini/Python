from tabulate import tabulate
import sys
import os
import csv

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py <filename.py>")


    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a csv file")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        table = convert_data(filename)


    except Exception as e:
        sys.exit(f"Error:{e}")

    print(table)

def convert_data(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            table = tabulate(data, headers="firstrow", tablefmt="grid")

        return table
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()

