numbers = input().split()
numbers_list = []

for num in numbers:
    numbers_list.append(num)

result = list(map(int,numbers_list))
print(sorted(result))