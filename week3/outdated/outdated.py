VALID_MONHTS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)


def main():
    print(format_date(*get_date()))


def parse_numeric_format(date):
    try:
        return tuple(map(int, date.split("/")))
    except ValueError:
        return None


def parse_text_format(date):
    if "," not in date:
        return None

    try:
        month, day, year = date.replace(",", "").split(" ")
    except ValueError:
        return None

    try:
        month = VALID_MONHTS.index(month) + 1
    except ValueError:
        return None

    return month, int(day), int(year)


def is_valid_date(month, day, year):
    return 0 < month < 13 and 0 < day < 32 and 0 <= year


def get_date():
    while True:
        date_input = input("Date: ").strip().title()

        date = parse_numeric_format(date_input) or parse_text_format(date_input)

        if not date or not is_valid_date(*date):
            continue

        return date


def format_date(month, day, year):
    return f"{year:04}-{month:02}-{day:02}"


main()
