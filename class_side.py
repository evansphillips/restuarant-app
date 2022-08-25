from class_item import Item

class Side(Item):
    """Side items on the menu."""

    def __init__(self, name, price, calories, p_time_mins, sauce=None):
        super().__init__(name, price, calories, p_time_mins)
        if sauce in {"Ketchup", "Mustard", "Ranch", "BBQ", "Teriyaki"}:
            self.sauce = sauce


