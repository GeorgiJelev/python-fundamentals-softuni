command = input()
coffee_needed = 0
while command.lower() != "end":
    if command.lower() == "coding" or command.lower() == "movie" \
            or command.lower() == "cat" or command.lower() == "dog":
        if command.islower():
            coffee_needed += 1
        else:
            coffee_needed += 2
    command = input()
if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)
