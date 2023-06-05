output = int(input())

for i in range(output):
    string = input()
    if "," in string or "." in string or "_" in string:
        print(f"{string} is not pure!")
        continue
    print(f"{string} is pure.")