import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    plate_pattern = re.compile(r'^[A-Za-z]{2,5}[1-9][0-9]*$|^[A-Za-z]{2,6}$')

    if plate_pattern.search(s) is None:
        return False

    return True


if __name__ == "__main__":
    main()
