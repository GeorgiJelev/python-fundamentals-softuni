def is_even(num):
    result = 0
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            result += int(num[i])
    return result


def is_odd(num):
    result = 0
    for i in range(len(num)):
        if int(num[i]) % 2 != 0:
            result += int(num[i])
    return result


number = input()
print(f"Odd sum = {is_odd(number)}, Even sum = {is_even(number)}")









