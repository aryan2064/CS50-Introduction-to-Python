import random

def main():
    level = getint("Level: ")
    number = random.randint(1, level)

    while True:
        guess = getint("Guess: ")

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break


def getint(prompt):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            continue

        if n > 0:
            return n

main()
