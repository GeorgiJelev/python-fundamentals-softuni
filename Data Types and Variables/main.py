n = int(input())
digits = 0
for num in range(n + 1):
    digits += num % 10
    if digits == 5 or digits == 7 or digits == 11:
        print(f"{digits} -> True")
    else:
        print(f"{digits} -> False")