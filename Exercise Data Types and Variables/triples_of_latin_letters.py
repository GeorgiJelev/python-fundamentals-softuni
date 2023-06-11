numbers_of_letters = int(input())

for first_number in range(numbers_of_letters):
    for second_number in range(numbers_of_letters):
        for third_number in range(numbers_of_letters):
            print(f"{chr(97 + first_number)}{chr(97 + second_number)}{chr(97 + third_number)}")