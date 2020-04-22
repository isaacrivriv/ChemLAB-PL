import periodic_table


class Compound:

    def __init__(self, elements, bond_type):
        # a dictionary with elements as keys and the number of atoms as values
        # i.e. {'H': 2, 'O': 1}
        self.elements = elements
        if bond_type == 'covalent':
            self.type = 'molecule'
        elif bond_type == 'ionic':
            self.type = 'ionic'
        elif bond_type == 'metallic':
            self.type = 'intermetallic'
        elif bond_type == 'coordinate covalent':
            self.type = 'complex'
        else:
            self.type = None

    def react(self, compound2):
        reaction = []
        return reaction

    def __str__(self):
        s = '['
        for x, y in self.elements.items():
            if y != 1:
                s += f'{x}_{y} '
            else:
                s += f'{x}'
        return s.rstrip() + f']\t type: {self.type}'


e1 = {'H': 2, 'O': 1}
print(Compound(e1, 'covalent'))
