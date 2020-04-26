from periodic_table import PERIODIC_TABLE


class Element:


    element_dic = {}
    atomic_num = 0
    symbol = ''
    name = ''
    group = 0
    period = 0
    atomic_weight = 0
    density = 0
    melting_point = ''
    boiling_point = ''
    heat_capacity = ''
    electronegativity = ''
    precise = ''
    type = ''


    #constructor
    def __init__(self,a_num):

        #Stores the dictionary with the info for the specific element
        self.element_dic = PERIODIC_TABLE[a_num]
        self.atomic_num = self.element_dic['atomic_num']
        self.symbol = self.element_dic['symbol']
        self.name = self.element_dic['name']
        self.group = self.element_dic['group']
        self.period = self.element_dic['period']
        self.atomic_weight = self.element_dic['atomic_weight']
        self.density = self.element_dic['density']
        self.melting_point = self.element_dic['melting_point']
        self.boiling_point = self.element_dic['boiling_point']
        self.heat_capacity = self.element_dic['heat_capacity']
        self.electronegativity = self.element_dic['electronegativity']
        self.precise = self.element_dic['precise']
        self.type = self.element_dic['type']

    def toString(self):
        concat = ''
        for key,value in self.element_dic.iteritems():
            concat = concat + key+ "=" + str(value)+ ","
        print(concat)

El = Element('10')
print(El.type)
