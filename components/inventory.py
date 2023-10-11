class Inventory:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) >= self.capacity:
            raise Exception("Inventory is full.")
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
