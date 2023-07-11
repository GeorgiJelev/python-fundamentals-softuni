names = input().split(", ")

sort_names = sorted(names, key=lambda x: (-len(x), x))
print(sort_names)
