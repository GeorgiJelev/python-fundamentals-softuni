class Inventory:

    def __init__(self, __capacity: int):
        self.items = []
        self.__capacity = __capacity

    def add_item(self, item: str, ):
        if self.__capacity > 0:
            self.__capacity -= 1
            self.items.append(item)
        return "not enough room in the inventory"

    def get_capacity(self):
        return len(self.items)

    def __repr__(self):
        self.item_string = ", ".join(self.items)
        return f"Items: {self.item_string}.\nCapacity left: {self.__capacity}"



inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
