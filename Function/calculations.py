


def calculation_func(first_number,second_number, operator):
    result = 0
    if operator == "multiply":
        result =  first_number * second_number
    elif operator == "divide":
        result = int(first_number // second_number)
    elif operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number

    return result


operator = input()
first_number = int(input())
second_number = int(input())
print(calculation_func(first_number , second_number  ,operator))