text = input("camelCase: ")
snake = []

for c in text:
    if c.isupper():
        snake.append("_")
    snake.append(c.lower())

snake = "".join(snake)
print(snake)
