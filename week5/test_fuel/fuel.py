def main():
    percentage = get_fuel_percentage()

    print(gauge(percentage))


def get_fuel_percentage():
    while True:
        fraction = input("Fraction: ")

        try:
            return convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)

    if x > y or x < 0 or y < 0:
        raise ValueError

    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage < 99:
        return f"{percentage:.0f}%"
    return "F"


if __name__ == "__main__":
    main()
