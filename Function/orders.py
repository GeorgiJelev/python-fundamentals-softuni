

def receive_orders(product:str, quantity: int):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2
    return f"{price * quantity:.2f}"

type_product = input()
product_quantity = int(input())
print(receive_orders(type_product , product_quantity))