lst = []

while True:
    command = input().split("-")
    if command[0] == "End":
        break

    priority = int(command[0])
    task = command[1]
    lst.append((priority, task))

sorted_task = [task_data[1] for task_data in sorted(lst)]
print(sorted_task)
