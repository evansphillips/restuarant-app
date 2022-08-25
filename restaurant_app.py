class Item:
    """Parent class that Initializes items
    with name, price, calories, and time (minutes) -- not directly used.
    """

    def __init__(self, name, price, calories, prep_time):
        self.name = str(name).title()
        self.price = round(float(price), 2)
        self.calories = int(calories)
        self.prep_time = prep_time

    def takeout_time(self, distance, speed):
        """Method that tells the customer how long their meal will 
        take to be ready for pickup based on prep_time, how far customer is (miles),
        and how fast they will arrive at the restaurant (mph).
        """
        arrival_time = distance / speed
        p_time_hrs = self.prep_time / 60
        if self.prep_time > arrival_time:
            print(
                f"Your order should be ready in {int(p_time_hrs * 60)} minutes. Estimated wait time: {int((p_time_hrs * 60) - (arrival_time * 60))} minutes."
            )
        else:
            print(f"Your order will be ready when you arrive!")

    def delivery_time(self, distance):
        """Method that tells the customer how long their meal will 
        take to arrive for delivery based on prep_time and how far customer is (miles)
        assuming the average speed our deliverers drive at is 30 mph.
        """
        total_time = self.prep_time + (distance / 30) * 60
        print(f"Your order should arrive in about {int(total_time)} minutes.")

    def __repr__(self):
        return self.name

    def currency_conversion(self, conversion, converted_price=None):
        """Currency converter for top 10 most common conversions with USD."""
        if conversion in {"euro", "EUR"}:
            self.converted_price = round(self.price * 0.842542, 2)
            print(
                f"This price of {self.price} USD is equal to {self.converted_price} {conversion}s"
            )
        elif conversion in {"British Pound", "GBP"}:
            self.converted_price = round(self.price * 0.720144, 2)
            print(
                f"This price of {self.price} USD is equal to {self.converted_price} {conversion}s"
            )
        elif conversion in {"Indian Rupee", "INR"}:
            self.converted_price = round(self.price * 74.490711, 0)
            print(
                f"This price of {self.price} USD is equal to {self.converted_price} {conversion}s"
            )
        elif conversion in {"Australian Dollar", "AUD"}:
            self.converted_price = round(self.price * 1.338357, 2)
            print(
                f"This price of {self.price} USD is equal to {self.converted_price} {conversion}s"
            )
        elif conversion in {"Canadian Dollar", "CAD"}:
            self.converted_price = round(self.price * 1.247326, 2)
            print(
                f"This price of {self.price} USD is equal to {self.converted_price} {conversion}s"
            )
        elif conversion in {"Singapore Dollar", "SGD"}:
            self.converted_price = round(self.price * 1.351209, 2)
            print(
                f"This price of {self.price} USD is equal to {self.converted_price} {conversion}s"
            )
        elif conversion in {"Swiss Franc", "CHF"}:
            self.converted_price = round(self.price * 0.914669, 2)
            print(
                f"This price of {self.price} USD is equal to {self.converted_price} {conversion}s"
            )
        elif conversion in {"Malaysian Ringgit", "MYR"}:
            self.converted_price = round(self.price * 4.190543, 2)
            print(
                f"This price of {self.price} USD is equal to {self.converted_price} {conversion}s"
            )
        elif conversion in {"Japanese Yen", "JPY"}:
            self.converted_price = round(self.price * 110.146124, 0)
            print(
                f"This price of {self.price} USD is equal to {self.converted_price} {conversion}s"
            )
        elif conversion in {"Chinese Yuan Renminbi", "CNY"}:
            self.converted_price = round(self.price * 6.473639, 2)
            print(
                f"This price of {self.price} USD is equal to {self.converted_price} {conversion}s"
            )


class food(item):
    """Non-liquid items on menu."""

    def __init__(self, name, price, calories, prep_time):
        super().__init__(name, price, calories, prep_time)


class side(item):
    """Side items on the menu."""

    def __init__(self, name, price, calories, prep_time, sauce=None):
        super().__init__(name, price, calories, prep_time)
        if sauce in {"Ketchup", "Mustard", "Ranch", "BBQ", "Teriyaki"}:
            self.sauce = sauce


class drink(item):
    """liquid items on menu."""

    def __init__(self, name, price, calories, prep_time, size=None):
        super().__init__(name, price, calories, prep_time)
        if size in {"S", "M", "L"}:
            self.size = size


class combo:
    """Combination of food, drink, and/or side"""

    def __init__(self, name, combo_items=[]):
        self.name = str(name).title()
        self.price = round(sum([i.price for i in combo_items]) * 0.9, 2)
        self.calories = sum([i.calories for i in combo_items])
        self.prep_time = sum([i.prep_time for i in combo_items])
        self.combo_items = combo_items

    def __repr__(self):
        return self.name


class Information:
    """All information that a customer would provide to the restaurant for pickup or delivery."""

    def __init__(self, customer_name, address, zip_code, phone_number, email_address):
        self.customer_name = customer_name
        self.address = address
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email_address = email_address
        if "@" not in email_address:
            raise Exception("Must list email address website.")

menu = {
    "Hamburger": food("Hamburger", 10, 500, 20),
    "Cheeseburger": food("Cheeseburger", 12.10, 550, 20),
    "Double-Cheeseburger": food("Double-Cheeseburger", 13, 600, 23),
    "Bacon Cheeseburger": food("Bacon Cheeseburger", 13, 750, 22),
    "Chicken Burger": food("Chicken Burger", 11.50, 450, 17),
    "Garden Burger": food("Garden Burger", 12.00, 300, 15),
    "8 Ct Chicken Nuggets": food("8 Ct Chicken Nuggets", 9.00, 300, 13),
    "12 Ct Chicken Nuggets": food("12 ct Chicken Nuggets", 10.50, 430, 15),
    "Egg Sandwhich": food("Egg Sandwhich", 8.00, 390, 14),
    "Egg Biscuit": food("Egg Biscuit", 7.50, 340, 14),
    "French Fries": side("French Fries", 3.00, 100, 5),
    "Nachos": side("Nachos", 2.00, 150, 8),
    "Onion Rings": side("Onion Rings", 2.50, 200, 5),
    "Mac and Cheese": side("Mac and Cheese", 3.00, 230, 7),
    "Tater Tots": side("Tater Tots", 2.50, 240, 6),
    "Hash Browns": side("Hash Browns", 1.50, 200,7),
    "Sprite": drink("Sprite", 2.00, 150, 1, "M"),
    "Coke": drink("Coke", 2.00, 1.50, 1, "M"),
    "Dr.Pepper": drink("Dr.Pepper", 2.00, 150, 1, "M"),
    "Fanta": drink("Fanta", 2.00, 150, 1, "M"),
    "Pepsi": drink("Pepsi", 2.00, 150, 1, "M"),
    "Mountain Dew": drink("Mountain Dew", 2.00, 200, "M"),
    "Root Beer": drink("Root Beer", 2.00, 150, "M"),
    "Diet Coke": drink("Diet Coke", 2.00, 150, "M"),
    "Bottled Water": drink("Bottled Water", 3.00, 0, 1, "M"),
    "Iced Coffee": drink("Iced Coffee", 2.50, 120, 1, "M"),
}

combos = {
    "Combo #1": combo(
        "Combo #1", [menu["Hamburger"], menu["French Fries"], menu["Coke"]]
    ),
    "Combo #2": combo(
        "Combo #2", [menu["Cheeseburger"], menu["Nachos"], menu["Sprite"]]
    ),
    "Combo #3": combo(
        "Combo #3", [menu["Chicken Burger"], menu["Onion Rings"], menu["Dr.Pepper"]]
    ),
    "Combo #4": combo(
        "Combo #4",
        [menu["Garden Burger"], menu["Mac and Cheese"], menu["Bottled Water"]],
    ),
    "Combo #5": combo(
        "Combo #5", [menu["Egg Sandwhich"], menu["Hash Browns"], menu["Iced Coffee"]]
    ),
    "Combo #6": combo(
        "Combo #6",
        [menu["8 Ct Chicken Nuggets"], menu["Tater Tots"], menu["Root Beer"]],
    ),
}