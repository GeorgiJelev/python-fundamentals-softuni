num = int(input())

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_POSITIVE = "positive"
COMMAND_NEGATIVE = "negative"

numbers = []
filtered_numbers = []

for _ in range(num):
    current_num = int(input())
    numbers.append(current_num)
command = input()

for num in numbers:
    filtered_command = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num < 0)
    )
    if filtered_command:
        filtered_numbers.append(num)
print(filtered_numbers)