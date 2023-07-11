def check_chairs(numbers_of_rooms):
    total_free_chairs = 0
    needed_chair = 0
    for number_of_room in range(1, numbers_of_room + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            total_free_chairs += difference
        else:
            needed_chair += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
    return total_free_chairs,needed_chair


numbers_of_room = int(input())
total_free_chairs, needed_chair = check_chairs(numbers_of_room)
if total_free_chairs >= needed_chair:
    print(f"Game On, {total_free_chairs} free chairs left")
