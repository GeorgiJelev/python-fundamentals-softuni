soft_version = [int(number) for number in input().split(".")]
soft_version[-1] += 1
for current_index in range(len(soft_version) -1, -1, -1):
    if soft_version[current_index] > 9:
        soft_version[current_index] = 0
        if current_index -1 >= 0:
            soft_version[current_index -1] += 1

print(".".join(str(number) for number in soft_version))