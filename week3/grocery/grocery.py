def main():
    grocery_list = get_grocery_list()

    print(format_grocery_list(grocery_list))


def get_grocery_list():
    list = {}

    while True:
        try:
            item = input().strip().lower()
        except EOFError:
            print()
            break

        list[item] = list.get(item, 0) + 1

    return list


def format_grocery_list(list):
    sorted_list = sorted(list)

    formatted_list = [f"{list[item]} {item.upper()}" for item in sorted_list]

    return "\n".join(formatted_list)


main()
