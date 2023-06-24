def sum_of_odd_digits(num):
    result = 0
    for i in range(len(num)):
        if int(num[i]) % 2 != 0:
            result += int(num[i])
    return result


def sum_of_even_digits(num):
    result = 0
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            result += int(num[i])
    return result


number = input()
print(f"Odd sum = {sum_of_odd_digits(number)}, Even sum = {sum_of_even_digits(number)}")