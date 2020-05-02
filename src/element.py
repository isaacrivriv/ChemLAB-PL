from src.periodic_table import PERIODIC_TABLE


class Element:

    def __init__(self, a_num):
        # Stores the dictionary with the info for the specific element
        self.element_data = PERIODIC_TABLE[a_num]

    def __str__(self):
        return self.element_data['symbol']

    def full_detail_str(self):
        return self.element_data.__str__()
