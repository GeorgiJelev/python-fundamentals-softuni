first_string = input()
second_string = input()
third_string = input()

animal = [first_string, second_string, third_string]
animal[0], animal[-1] = animal[-1], animal[0]
print(animal)
