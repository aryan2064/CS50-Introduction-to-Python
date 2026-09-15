import inflect, sys

from datetime import datetime, date


def main():
    date_user = input("Date of Birth: ")

    if not (date_user := validate_date(date_user)):
        sys.exit("Invalid date")

    date_today = date.today()

    difference = calculate_minutes_difference(date_user, date_today)

    print(format_minutes(difference))


def validate_date(d):
    try:
        return datetime.strptime(d, "%Y-%m-%d").date()
    except ValueError:
        return None


def calculate_minutes_difference(start_date, end_date):
    return round((end_date - start_date).total_seconds() / 60)


def format_minutes(minutes):
    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword='')} minutes".capitalize()


if __name__ == "__main__":
    main()
