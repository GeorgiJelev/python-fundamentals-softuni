factor = int(input())
count = int(input())

numbers_list = []
for num in range(1, count + 1):
    numbers_list.append(factor * num)
print(numbers_list)