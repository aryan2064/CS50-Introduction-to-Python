import csv, sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    filepath_before, filepath_after = sys.argv[1], sys.argv[2]
    if not filepath_before.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filepath_before) as file_before, open(
            filepath_after, "w"
        ) as file_after:
            reader = csv.DictReader(file_before)
            writer = csv.DictWriter(file_after, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {filepath_before}")


if __name__ == "__main__":
    main()
