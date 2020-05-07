from periodic_table import PERIODIC_TABLE


class Element:

    # constructor
    def __init__(self,a_num):
        # Stores the dictionary with the info for the specific element
        self.dictionary = PERIODIC_TABLE[a_num]
        
    def __str__(self):
        # return self.element_data['symbol']
        return self.full_detail_str()

    def full_detail_str(self):
        return self.dictionary.__str__()


