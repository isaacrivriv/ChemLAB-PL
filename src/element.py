from periodic_table import PERIODIC_TABLE


class Element:

    # constructor
    def __init__(self,e):
        # Stores the dictionary with the info for the specific element
        try:
            self.dictionary = PERIODIC_TABLE[e]
        except KeyError:
            for _, d in PERIODIC_TABLE.items():
                if d['symbol'] == e:
                    self.dictionary = d
        
    def __str__(self):
        # return self.element_data['symbol']
        return self.full_detail_str()

    def full_detail_str(self):
        return self.dictionary.__str__()


