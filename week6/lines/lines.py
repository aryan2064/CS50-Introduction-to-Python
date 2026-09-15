import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filepath = sys.argv[1]
    if not filepath.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filepath) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    program_lines = [
        line for line in lines if line.strip() and not line.strip().startswith("#")
    ]

    print(len(program_lines))


if __name__ == "__main__":
    main()
