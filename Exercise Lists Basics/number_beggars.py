sum_list_string = input().split(", ")
count_of_beggars = int(input())
final_list = []
counter_of_index = 0
sum_list_as_digit = []
for element in sum_list_string:
    sum_list_as_digit.append(int(element))
while counter_of_index < count_of_beggars:
    sum_for_current_begar = 0
    for current_index in range(counter_of_index , len(sum_list_as_digit) , count_of_beggars):
        sum_for_current_begar += sum_list_as_digit[current_index]
    counter_of_index +=1
    final_list.append(sum_for_current_begar)
print(final_list)



