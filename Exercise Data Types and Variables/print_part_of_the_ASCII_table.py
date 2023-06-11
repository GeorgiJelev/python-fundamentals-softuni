start_index = int(input())
stop_index = int(input())
final_string = ""

for character in range(start_index, stop_index + 1):
    final_string += chr(character) + " "
print(final_string)