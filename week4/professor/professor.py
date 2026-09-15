import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        score += get_question_score(x, y)

    print(f"Score: {score}")


def get_question_score(x, y):
    answer = x + y

    for _ in range(3):
        try:
            guess = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
            continue

        if guess == answer:
            return 1

        print("EEE")

    print(f"{x} + {y} = {answer}")
    return 0


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        except EOFError:
            return 1

        if level in [1, 2, 3]:
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

    raise ValueError


if __name__ == "__main__":
    main()
