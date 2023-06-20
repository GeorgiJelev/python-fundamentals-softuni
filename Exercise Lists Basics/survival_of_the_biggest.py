numbers_as_digits = list(int(i) for i in input().split())
remover = int(input())

for _ in range(remover):
    numbers_as_digits.remove(min(numbers_as_digits))
print(*numbers_as_digits, sep=", ")