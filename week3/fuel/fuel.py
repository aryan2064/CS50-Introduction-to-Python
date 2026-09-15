def main():
    percentage = get_fuel_percentage()

    print(get_message(percentage))


def get_fuel_percentage():
    while True:
        fraction = input("Fraction: ")

        try:
            x, y = fraction.split("/")
            x, y = int(x), int(y)
        except ValueError:
            continue

        if x > y or x < 0 or y < 0:
            continue

        try:
            return x / y * 100
        except ZeroDivisionError:
            continue


def get_message(percentage):
    if percentage <= 1:
        return "E"
    if percentage < 99:
        return f"{percentage:.0f}%"
    return "F"


main()
