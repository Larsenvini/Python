import sys
import os
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too many command-line arguments")

    original_filename = sys.argv[1]
    new_filename = sys.argv[2]

    if not original_filename.endswith(".csv"):
        sys.exit("Original file is not a csv file")

    if not new_filename.endswith(".csv"):
        sys.exit("New file is not a csv file")

    if not os.path.isfile(original_filename):
        sys.exit(f"Could not read {original_filename}")

    try:
        table = scourgify(original_filename)
        transfer(new_filename, table)

    except Exception as e:
        sys.exit(f"Error:{e}")



def scourgify(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                last, first = row["name"].split(", ")
                data.append({"first": first, "last": last, "house": row["house"]})

        return data

    except Exception as e:
        raise e

def transfer(new_filename, data):
    try:
        with open(new_filename, "w", newline = "") as file:
            fieldnames = ["first","last", "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()
