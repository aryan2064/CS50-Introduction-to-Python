def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.strip().lower()

    if greeting.startswith("hello"):
        return 0

    try:
        if greeting[0] == "h":
            return 20
    except IndexError:
        pass

    return 100


if __name__ == "__main__":
    main()
