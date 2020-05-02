from periodic_table import PERIODIC_TABLE


class Element:



    #constructor
    def __init__(self,a_num):

        #Stores the dictionary with the info for the specific element
        self.dictionary = PERIODIC_TABLE[a_num]


    def _str_(self):
        concat = ''
        for key,value in self.iteritems():
            concat = concat + key+ "=" + str(value)+ ","
        return (concat)
