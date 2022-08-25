class CustomerInformation:
    """All information that a customer would provide to the restaurant for pickup or delivery.
    """


    def __init__(self, info_dict=None):
        if info_dict is None:
            info_dict = {}
        self.info_dict = info_dict

    def add_info(self, key, value):
        """Take in a string for a key and values, adds informationb to info_dict
        """
        self.info_dict.update({key: value})

    def show_info_dict(self):
        """getter method for info_dict"""
        print(self.info_dict)

    def __repr__(self):
        """Represents each user uniquely by their email because it is likely to be most distinct information item
        """
        return self.email_address