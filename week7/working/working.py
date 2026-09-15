import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_pattern = re.compile(
        r"(?P<beggining_time>(?:0?[1-9]|1[0-2])(?::[0-5]\d)? [ap])M to (?P<ending_time>(?:0?[1-9]|1[0-2])(?::[0-5]\d)? [ap])M",
        re.IGNORECASE,
    )

    if not (match := re.search(time_pattern, s)):
        raise ValueError("Invalid time format")

    beggining_time, ending_time = format_time(
        match.group("beggining_time")
    ), format_time(match.group("ending_time"))

    return f"{beggining_time} to {ending_time}"


def format_time(time):
    hour_minute_meridiem_pattern = re.compile(
        r"(?P<hours>\d+):?(?P<minutes>\d+)? (?P<meridiem>[ap])", re.IGNORECASE
    )

    match = re.search(hour_minute_meridiem_pattern, time)

    hours, minutes, meridiem = (
        match.group("hours"),
        match.group("minutes"),
        match.group("meridiem"),
    )

    if not minutes:
        minutes = "0"

    if meridiem.lower() == "a":
        hours = format_am_hour(hours)
    else:
        hours = format_pm_hour(hours)

    return f"{hours.zfill(2)}:{minutes.zfill(2)}"


def format_am_hour(hour):
    return hour if hour != "12" else "0"


def format_pm_hour(hour):
    return hour if hour == "12" else str(int(hour) + 12)


if __name__ == "__main__":
    main()
