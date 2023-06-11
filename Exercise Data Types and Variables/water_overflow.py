number_of_lines = int(input())
water_capacity = 255
water_counter = 0
for i in range(number_of_lines):
    current_litter = int(input())
    if water_capacity - current_litter < 0:
        print("Insufficient capacity!")
        continue
    water_counter += current_litter
    water_capacity -= current_litter
print(water_counter)