from element import Element


class Compound:

    def __init__(self, elements, bond_type):
        # a dictionary with elements as keys and the number of atoms as values
        # i.e. {'H': 2, 'O': 1}
        self.elements = elements
        self.mass = self.calculate_mass()       # given as a tuple (mass quantity, mass unit)
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

    def __str__(self):
        s = '['
        for x, y in self.elements.items():
            if y != 1:
                s += f'{x}_{y} '
            else:
                s += f'{x}'
        return s.rstrip() + f'] \ttype: {self.type} \tmass: {self.mass[0]}'

    def calculate_mass(self):
        mass = 0
        for e in self.elements:
            mass += Element(e).info['atomic_weight'] * self.elements[e]
        return mass, 'g/mol'
