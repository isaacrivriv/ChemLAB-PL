from periodic_table import PERIODIC_TABLE


class Element:

    # constructor
    def __init__(self,a_num):
        # Stores the dictionary with the info for the specific element
        self.dictionary = PERIODIC_TABLE[a_num]

    def __str__(self):
        concat = ''
        for key, value in self.dictionary.items():
            concat = concat + key + "=" + str(value) + ", "
        return concat
