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
        else:
            self.type = None

    def __str__(self):
        substring = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        s = '['
        for x, y in self.elements.items():
            if y != 1:
                s += f'{x}{y}'
            else:
                s += f'{x}'
            s += f' , '
        return s.rstrip().translate(substring) + f'] \ttype: {self.type}'

    def calculate_mass(self):
        mass = 0
        for e in self.elements:
            mass += e.dictionary['atomic_weight'] * self.elements[e]  # e is wrong, must be a number
        return mass, 'g/mol'

    def percent_composition(self, e):
        if e not in self.elements:
            raise ValueError(str(e) + " is not part of this compound.")

        return e.dictionary['atomic_weight'] / self.mass[0] * 100, '%'

    def convertToBalanceFormat(self):
        copy = {}
        for key in self.elements:
            copy[key.dictionary['symbol']]=self.elements[key]
        return copy
