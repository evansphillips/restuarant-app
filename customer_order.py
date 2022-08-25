from class_information import CustomerInformation
from class_menu import Menu


class CustomerOrder:
    """Keep track of and add orders and prices to dictionary."""

    def __init__(self, order_history=None, total_price=0):

        if order_history == None:
            order_history = {}
            self.total_price = total_price
        self.menu = Menu()
        self.local_currency = "USD"
        self.order_history = order_history
        self.info = CustomerInformation()

    def __repr__(self):
        return str(self.order_history)

    def string_to_item(self, item_name):
        """Determines if an item name actually exists in the menu and accountw for duck typing with removal of case sensitivity
        """
        new_dict_lower = dict((k.lower(), v) for k, v in self.menu.menu.items())
        item = self.menu.menu.get(item_name) or new_dict_lower.get(item_name)
        if item is None:
            print(f"Item {item_name} not in menu. Please enter a valid item.")
            return
        return item

    def show_total_price(self):
        """Displays total price for all quantities of items in self.order_history in the specified form of currency
        """
        print(f"{self.total_price} {self.local_currency}")

    def add_item(self):
        """Add item to self.order_history dict with item name as key and number of items as value
        """
        self.show_menu()
        # Ask customer what they want
        selected_item = str(
            input(
                "\nWhat would you like to order today? One item at a time, please. Quantity is the next question.\n\n"
            )
        )
        item = self.string_to_item(selected_item)
        if item:
            number = int(input(f"\n\nHow many {item}s would you like to order?\n\n"))
        else:
            return self.add_item()
        old_qty = self.order_history.get(item, 0)
        self.order_history[item] = old_qty + number
        self.total_price += item.converted_price(self.local_currency) * number
        self.show_order()

    def remove_item(self):
        """This function makes sure that the quantity I remove is not 
        greater than the quantity I have. Adjusts order_history and total_price accordingly.
        """
        # ask customer what they want to remove
        item_name = str(input("\nWhat item would you like to remove?\n\n"))
        # check if specified item is in my list of items
        item = self.string_to_item(item_name)
        if item:
            number = int(input(f"\n\nHow many {item}s would you like to remove?\n\n"))
        else:
            return self.add_item()
        actually_deleted = min(number, self.order_history[item])
        self.order_history[item] -= actually_deleted
        self.total_price -= item.converted_price(self.local_currency) * actually_deleted
        self.show_order()

    def update_payment(self, cust_info=None):
        """Tells the user what credit card we have on file and gives them the choice to change it. This displays the last 4 digits of the credit card for safety reasons
        """
        cc_num = str(self.info.info_dict["Customer Credit Card Number"])
        print("The CC on file ends with: ", cc_num[-4:])
        answer = input("\n\nWould you like to use this credit card? y/n\n\n")
        if "n" in answer.lower():
            new_cc_num = str(
                input("\n\nPlease input a new 16 digit credit card number: \n\n")
            )
            self.info.info_dict["Customer Credit Card Number"] = new_cc_num
            print("The new CC on file ends with: ", new_cc_num[-4:])
        elif "y" in answer.lower():
            print("CC on file: ", cc_num[-4:])
        else:
            raise Exception("Please enter a valid response.")

    def show_menu(self):
        """Displays the menu int the specified local currency"""
        print(self.menu.show(self.local_currency))

    def show_order(self):
        """To do: display order history prettier with prices."""
        print(f"\nGreat! So far, your order consists of: ")
        print(self.order_history)
        print(f"\nwith a total of {self.total_price} {self.local_currency}")

    def begin_order(self):
        """This is the main function IT DOES EVERYTHING -- runs other functions to go through the conversation flow of ordering"""
        # welcome them and get local currency
        self.get_currency()
        self.add_item()
        while True:
            self.get_next_action()
            if decision == "exit":
                break

    def get_next_action(self):
        """Gives options to subtract or add items from order_history as well as record personal information to continue to the end of the process. If the user types 'exit', the program terminates.
        """
        global decision
        decision = str(input("\n\nWhat would you like to do? add/remove/pay/exit\n\n"))
        if decision == "add":
            self.add_item()
        elif decision == "remove":
            self.remove_item()
        elif decision == "pay":
            self.record_payment()
        
    

    def record_payment(self):
        """Adds name, address, email address, phone number, and credit card number to an empty dictionary called self.info
        """
        customer_name = str(
            input(
                "\n\nWe're almost there! Now it's time to get your information. Please input your name.\n\n"
            )
        )
        self.info.add_info("Customer name", customer_name)

        address = str(input("\n\nPlease input your address.\n\n"))
        self.info.add_info("Customer Address", address)
        phone_number = str(input("\n\nPlease input a 10 digit phone number.\n\n"))
        self.info.add_info("Customer Phone Number", phone_number)
        email_address = str(input("\n\nPlease enter your email address.\n\n"))
        self.info.add_info("Customer Email Address", email_address)
        credit_card_no = str(input("\n\nPlease enter a 16 digit credit card number.\n\n"))
        self.info.add_info("Customer Credit Card Number", credit_card_no)
        self.info.show_info_dict()
        check_info = str(
            input(f"\n\nThank you! Does the information displayed look correct? y/n\n\n")
        )
        if check_info == "y":
            cc_num = str(self.info.info_dict["Customer Credit Card Number"])
            print("The CC on file ends with: ", cc_num[-4:])
            answer = input("\n\nWould you like to use this credit card? y/n\n\n")
            if "n" in answer.lower():
                new_cc_num = str(
                    input("\n\nPlease input a new 16 digit credit card number: \n\n")
                )
                self.info.info_dict["Customer Credit Card Number"] = new_cc_num
                print("The new CC on file ends with: ", new_cc_num[-4:])
            elif "y" in answer.lower():
                print("CC on file: ", cc_num[-4:])
            else:
                raise Exception("Please enter a valid response.")
            self.delivery_time()

        elif check_info == "n":
            self.continue_info_dict_edit()

    def continue_info_dict_edit(self):
        """Prompts user if they want to edit the information dictionary
        """
        finish = str(input("\n\n do you have another information item you would like to edit? y/n\n\n"))
        while finish.lower() == "y":
            self.replace_info_dict()
        self.delivery_time()

    def replace_info_dict(self):
        """function that replaces the information in a info_dict
        """
        replace = str(
            input("\n\nwhat would you like to replace? name/address/phone/email/card\n\n")
        )
        if replace.lower() == "name":
            new_name = str(
                input("\n\nWhat would you like to replace the Name section with?\n\n")
            )
            self.info.info_dict["Custonmer name"] = new_name
            print(f"\nGreat! Your new info is now:")
            self.info.show_info_dict()
            self.continue_info_dict_edit()

        elif replace.lower() == "address":
            new_address = str(
                input("\n\nWhat would you like to replace the address section with?\n\n")
            )
            self.info.info_dict["Customer Address"] = new_address
            print(f"\nGreat! Your new info is now:")
            self.info.show_info_dict()
            self.continue_info_dict_edit()

        elif replace.lower() == "phone":
            new_phone = str(
                input("\n\nWhat would you like to replace the phone number section with?\n\n")
            )
            self.info.info_dict["Customer Phone Number"] = new_phone
            print(f"\nGreat! Your new info is now:")
            self.info.show_info_dict()
            self.continue_info_dict_edit()

        elif replace.lower() == "email":
            new_email = str(
                input("\n\nWhat would you like to replace the email section with?\n\n")
            )
            self.info.info_dict["Customer Email Address"] = new_email
            print(f"\nGreat! Your new info is now:")
            self.info.show_info_dict()
            self.continue_info_dict_edit()

        elif replace.lower() == "card":
            self.update_payment()
            print(f"\nGreat! Your new info is now:")
            self.info.show_info_dict()
            self.continue_info_dict_edit()

    def get_currency(self):
        """Getter method to display the options of currency available for conversion
        """
        print("Welcome to Evan's! what's your local currency?")
        print("\nUSD, EUR, GBP, INR, AUD, CAD, SGD, CHF, MYR, JPY, CNY")
        local_currency = input()
        self.local_currency = local_currency.upper()

    def takeout_time(self, distance, speed):
        """Method that tells the customer how long their meal will 
        take to be ready for pickup based on p_time_mins, how far customer is (miles),
        and how fast they will arrive at the restaurant (mph).
        """
        arrival_time = distance / speed
        p_time_hrs = self.p_time_mins / 60
        if p_time_hrs > arrival_time:
            print(
                f"\nYour order should be ready in {int(p_time_hrs * 60)} minutes. Estimated wait time: {int((p_time_hrs * 60) - (arrival_time * 60))} minutes."
            )
        else:
            print(f"\nYour order will be ready when you arrive!")

    def delivery_time(self):
        """Method that tells the customer how long their meal will 
        take to arrive for delivery based on p_time_mins and how far customer is (miles)
        assuming the average speed our deliverers drive at is 30 mph.
        """
        # Using list comprehension to find the maximum prep time of all items in order_history and using that as an estimate for the prep time fo the entire order
        max_p_time_mins = max(
            [self.get_p_time_mins(item) for item in self.order_history]
        )
        choice = str(
            input(
                "\n\nThank you. Would you like these items for takeout or delivery? takeout/delivery\n\n"
            )
        )
        if choice == "takeout":
            print(
                f"\nYour order will be ready in {max_p_time_mins} minutes, thank you for your order! Have a nice day."
            )
            self.get_next_action()
        elif choice == "delivery":
            distance = int(
                input("\n\nHow far away are you from our restaurant? (in miles)\n\n")
            )
            total_time = max_p_time_mins + (distance / 30) * 60
            print(
            f"\nTaking the prep time of your order into account and because our drivers drive at about 30 mph, Your order should arrive at your door in about {int(total_time)} minutes! Have a nice day."
        )
            self.get_next_action()

            
            
    def get_p_time_mins(self, item):
        """Accesses the prepration time (prep_time) attribute of an item"""
        return self.menu.menu[str(item)].p_time_mins