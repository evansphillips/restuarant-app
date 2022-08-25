class Combo:
    """Combination of food, drink, and/or side"""

    def __init__(self, name, combo_items=[]):
        self.name = str(name).title()
        self.price = round(sum([i.price for i in combo_items]) * 0.9, 2)
        self.calories = sum([i.calories for i in combo_items])
        self.p_time_mins = sum([i.p_time_mins for i in combo_items])
        self.combo_items = combo_items

    def converted_price(self, convert_to="USD"):
        """Converts price from USD to 10 other choice of currency."""
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
            print(
                "Not a valid currency. Please make sure you are using correct abbreviations."
            )
            return None
        return round(self.price * conversion_factor, 2)

    def __repr__(self):
        return self.name
    
    