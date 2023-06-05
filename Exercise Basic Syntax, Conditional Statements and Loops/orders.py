output = int(input())
total_price = 0
for i in range(output):
    capsule_per_price = float(input())
    days = int(input())
    capsule_needed_per_day = int(input())
    if capsule_per_price < 0.01 or capsule_per_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_needed_per_day < 1 or capsule_needed_per_day > 2000:
        continue
    total_cost_for_coffee = (days * capsule_needed_per_day) * capsule_per_price
    total_price += total_cost_for_coffee
    print(f"The price for the coffee is: ${total_cost_for_coffee:.2f}")
print(f"Total: ${total_price:.2f}")




