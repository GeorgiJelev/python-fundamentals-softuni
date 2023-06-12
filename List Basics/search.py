numbers_of_string = int(input())
word = input()
strings = []

for _ in range(numbers_of_string):
    current_string = input()
    strings.append(current_string)
print(strings)
for i in range(len(strings) -1, -1, -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)
print(strings)
