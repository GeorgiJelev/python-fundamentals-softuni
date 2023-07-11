numbers_of_wagons = int(input())
wagons = [0] * numbers_of_wagons


while True:
    command = input()

    if command == "End":
        break
    data = command.split(" ")
    current_command = data[0]

    if current_command == "add":
        people_to_add = data[1]
        wagons[-1] = int(people_to_add)
    elif current_command == "insert":
        index = int(data[1])
        numbers_of_people = int(data[2])
        wagons[index] += numbers_of_people
    elif current_command == "leave":
        index = int(data[1])
        numbers_of_people = int(data[2])
        wagons[index] -= numbers_of_people

print(wagons)
