class Item:
    """Parent class that Initializes items
    with name, price, calories, and time (minutes) -- not directly used.
    """

    def __init__(self, name, price, calories, p_time_mins):
        """Initializing name, price, calories, and prep time of each item"""
        self.name = str(name).title()
        self.price = round(float(price), 2)
        self.calories = int(calories)
        self.p_time_mins = p_time_mins

    def __repr__(self):
        """Represents Item as its name"""
        return self.name

    def converted_price(self, convert_to="USD"):
        """Returns the converted price of an item based on its original price in USD
        """
        exchange_rates = {
            "USD": 1.00,
            "EUR": 0.842542,
            "GBP": 0.720144,
            "INR": 74.490711,
            "AUD": 1.338357,
            "CAD": 1.247326,
            "SGD": 1.351209,
            "CHF": 0.914669,
            "MYR": 4.190543,
            "JPY": 110.146124,
            "CNY": 6.473639,
        }
        conversion_factor = exchange_rates.get(convert_to, None)

        if conversion_factor is None:
            print("Not a valid currency. Please make sure you are using abbreviations.")
            return None
        return round(self.price * conversion_factor, 2)