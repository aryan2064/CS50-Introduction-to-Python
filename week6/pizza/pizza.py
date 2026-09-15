import csv, sys

from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filepath = sys.argv[1]
    if not filepath.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filepath) as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
