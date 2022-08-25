from class_item import Item


class Drink(Item):
    """liquid items on menu."""

    def __init__(self, name, price, calories, p_time_mins, size=None):
        super().__init__(name, price, calories, p_time_mins)
        self.size = size
    
    def get_size(self, size):
         if size in {"S", "M", "L"}:
                self.size = size
        