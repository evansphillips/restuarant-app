from class_item import Item

class Food(Item):
    """Non-liquid items on menu."""

    def __init__(self, name, price, calories, p_time_mins):
        super().__init__(name, price, calories, p_time_mins)
        self.p_time_mins = p_time_mins

