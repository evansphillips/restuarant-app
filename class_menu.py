from class_item import Item
from class_combo import Combo


single_items = {
    "Hamburger": Item("Hamburger", 10, 500, 20),
    "Cheeseburger": Item("Cheeseburger", 12.10, 550, 20),
    "Double-Cheeseburger": Item("Double-Cheeseburger", 13, 600, 23),
    "Bacon Cheeseburger": Item("Bacon Cheeseburger", 13, 750, 22),
    "Chicken Burger": Item("Chicken Burger", 11.50, 450, 17),
    "Garden Burger": Item("Garden Burger", 12.00, 300, 15),
    "8 Ct Chicken Nuggets": Item("8 Ct Chicken Nuggets", 9.00, 300, 13),
    "12 Ct Chicken Nuggets": Item("12 ct Chicken Nuggets", 10.50, 430, 15),
    "Egg Sandwhich": Item("Egg Sandwhich", 8.00, 390, 14),
    "Egg Biscuit": Item("Egg Biscuit", 7.50, 340, 14),
    "French Fries": Item("French Fries", 3.00, 100, 5),
    "Nachos": Item("Nachos", 2.00, 150, 8),
    "Onion Rings": Item("Onion Rings", 2.50, 200, 5),
    "Mac and Cheese": Item("Mac and Cheese", 3.00, 230, 7),
    "Tater Tots": Item("Tater Tots", 2.50, 240, 6),
    "Hash Browns": Item("Hash Browns", 1.50, 200, 7),
    "Sprite": Item("Sprite", 2.00, 150, 1),
    "Coke": Item("Coke", 2.00, 150, 1),
    "Dr.Pepper": Item("Dr.Pepper", 2.00, 150, 1),
    "Fanta": Item("Fanta", 2.00, 150, 1),
    "Pepsi": Item("Pepsi", 2.00, 150, 1),
    "Mountain Dew": Item("Mountain Dew", 2.00, 200, 1),
    "Root Beer": Item("Root Beer", 2.00, 150, 1),
    "Diet Coke": Item("Diet Coke", 2.00, 150, 1),
    "Bottled Water": Item("Bottled Water", 3.00, 0, 1),
    "Iced Coffee": Item("Iced Coffee", 2.50, 120, 1),
}


class Menu(dict):
    """Class representing all food, drinks, combos and sides"""
    def __init__(self):
        self.menu = {
            #            Item(name, price, calories, prep_time)
            "Hamburger": Item("Hamburger", 10, 500, 20),
            "Cheeseburger": Item("Cheeseburger", 12.10, 550, 20),
            "Double-Cheeseburger": Item("Double-Cheeseburger", 13, 600, 23),
            "Bacon Cheeseburger": Item("Bacon Cheeseburger", 13, 750, 22),
            "Chicken Burger": Item("Chicken Burger", 11.50, 450, 17),
            "Garden Burger": Item("Garden Burger", 12.00, 300, 15),
            "8 Ct Chicken Nuggets": Item("8 Ct Chicken Nuggets", 9.00, 300, 13),
            "12 Ct Chicken Nuggets": Item("12 ct Chicken Nuggets", 10.50, 430, 15),
            "Egg Sandwhich": Item("Egg Sandwhich", 8.00, 390, 14),
            "Egg Biscuit": Item("Egg Biscuit", 7.50, 340, 14),
            "French Fries": Item("French Fries", 3.00, 100, 5),
            "Nachos": Item("Nachos", 2.00, 150, 8),
            "Onion Rings": Item("Onion Rings", 2.50, 200, 5),
            "Mac and Cheese": Item("Mac and Cheese", 3.00, 230, 7),
            "Tater Tots": Item("Tater Tots", 2.50, 240, 6),
            "Hash Browns": Item("Hash Browns", 1.50, 200, 7),
            "Sprite": Item("Sprite", 2.00, 150, 1),
            "Coke": Item("Coke", 2.00, 1.50, 1),
            "Dr.Pepper": Item("Dr.Pepper", 2.00, 150, 1),
            "Fanta": Item("Fanta", 2.00, 150, 1),
            "Pepsi": Item("Pepsi", 2.00, 150, 1),
            "Mountain Dew": Item("Mountain Dew", 2.00, 200, 1),
            "Root Beer": Item("Root Beer", 2.00, 150, 1),
            "Diet Coke": Item("Diet Coke", 2.00, 150, 1),
            "Bottled Water": Item("Bottled Water", 3.00, 0, 1),
            "Iced Coffee": Item("Iced Coffee", 2.50, 120, 1),
            "Combo #1": Combo(
                "Combo #1",
                [
                    single_items["Hamburger"],
                    single_items["French Fries"],
                    single_items["Coke"],
                ],
            ),
            "Combo #2": Combo(
                "Combo #2",
                [
                    single_items["Cheeseburger"],
                    single_items["Nachos"],
                    single_items["Sprite"],
                ],
            ),
            "Combo #3": Combo(
                "Combo #3",
                [
                    single_items["Chicken Burger"],
                    single_items["Onion Rings"],
                    single_items["Dr.Pepper"],
                ],
            ),
            "Combo #4": Combo(
                "Combo #4",
                [
                    single_items["Garden Burger"],
                    single_items["Mac and Cheese"],
                    single_items["Bottled Water"],
                ],
            ),
            "Combo #5": Combo(
                "Combo #5",
                [
                    single_items["Egg Sandwhich"],
                    single_items["Hash Browns"],
                    single_items["Iced Coffee"],
                ],
            ),
            "Combo #6": Combo(
                "Combo #6",
                [
                    single_items["8 Ct Chicken Nuggets"],
                    single_items["Tater Tots"],
                    single_items["Root Beer"],
                ],
            ),
        }

    def __repr__(self):
        """Represents the menu as a string"""
        return str(self.menu)

    def show(self, local_currency="USD"):
        """Displays design for the menu in item - (calories)........price format"""
        n = 1
        # Converting price based on local currency
        for item_name, item in self.menu.items():
            converted_price = item.converted_price(local_currency)
            if local_currency == "USD":
                print(
                    f"{n}. {item} - ({item.calories} cal)......... ${converted_price}0"
                )
                n += 1
            else:
                print(
                    f"{n}. {item} - ({item.calories} cal)......... {converted_price} {local_currency}"
                )
                n += 1