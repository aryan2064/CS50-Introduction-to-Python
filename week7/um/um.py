import re


def main():
    print(count(input("Text: ")))


def count(s):
    um_instances = re.findall(r"\bum\b", s, re.IGNORECASE)

    return len(um_instances)


if __name__ == "__main__":
    main()
