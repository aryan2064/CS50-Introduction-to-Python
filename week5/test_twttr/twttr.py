def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    vowels = ("a", "e", "i", "o", "u")

    no_vowels = [char for char in word if char.lower() not in vowels]

    return "".join(no_vowels)


if __name__ == "__main__":
    main()
