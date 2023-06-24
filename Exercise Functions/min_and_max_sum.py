numbers = input().split(" ")

list_of_digit = [int(item) for item in numbers]

print(f"The minimum number is {min(list_of_digit)}")
print(f"The maximum number is {max(list_of_digit)}")
print(f"The sum number is: {sum(list_of_digit)}")