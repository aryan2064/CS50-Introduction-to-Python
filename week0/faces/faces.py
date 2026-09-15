def convert (word):
    word = word.replace(":)", "🙂").replace(":(", "🙁")
    return word

def main():
    word = input()
    print(convert(word))

main()
