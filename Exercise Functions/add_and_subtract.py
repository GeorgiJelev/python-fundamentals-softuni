def sum_numbers(a, b):
    return a + b


def subtract(sum , third):
    return sum - third_num


def add_and_subtract(a, b, c):
    sum_of_the_first_and_second_int = sum_numbers(first_num, second_num)
    result = subtract(sum_of_the_first_and_second_int, third_num)
    return result

first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))