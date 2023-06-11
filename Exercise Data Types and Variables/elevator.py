import math
elevator_capacity = int(input())
capacity_people = int(input())

total = elevator_capacity / capacity_people
print(math.ceil(total))