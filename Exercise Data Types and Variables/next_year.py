year = int(input())
condition = False

while not condition:
    year += 1
    set_year = set()

    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    condition = len(set_year) == len(str(year))

print(year)