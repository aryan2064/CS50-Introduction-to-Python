def main():
    time = convert(input("What time is it? "))

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    if "m" in minutes:
        minutes, am_pm = minutes.split(" ")
        if "p" in am_pm:
            hours = int(hours) + 12

    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
