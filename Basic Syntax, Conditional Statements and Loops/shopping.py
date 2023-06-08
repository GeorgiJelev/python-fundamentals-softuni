budget = int(input())
price_product = input()

while price_product != "End":
    current_price = int(price_product)
    budget -= current_price
    if budget < 0:
        print("You went in overdraft")
        break
    price_product = input()

else:
    print("You bought everything you needed")