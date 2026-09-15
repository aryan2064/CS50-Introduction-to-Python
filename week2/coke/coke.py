valid_coins = ("25", "10", "5")

amount_due = 50
coins_amount = 0

while True:
    print(f"Amount Due: {amount_due - coins_amount}")

    coin = input("Insert Coin: ")

    if coin not in valid_coins:
        continue

    coins_amount += int(coin)

    if coins_amount >= amount_due:
        break

print(f"Change Owed: {coins_amount - amount_due}")
