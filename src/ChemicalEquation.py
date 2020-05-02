from sympy import Matrix, linsolve


class EquationSide:

    def __init__(self, list_compounds, list_coefficient=None):
        if type(list_compounds) == dict:
            list_compounds = (list_compounds,)
        self.num_terms = len(list_compounds)
        if list_coefficient is None:
            list_coefficient = [1] * self.num_terms
        if len(list_coefficient) == self.num_terms:
            self.coefficients = list_coefficient
            self.compounds = list_compounds

    def isReactant(self):
        return None

    def isProduct(self):
        return None

    def get_list_of_elements(self):
        elements_name = set()
        for compound in self.compounds:
            elements_name.update(compound.keys())
        return list(elements_name)

    def get_coefficients(self):
        return self.coefficients

    def get_elements_atoms_count(self):
        atoms_count = {}
        for compound, coeff in zip(self.compounds, self.coefficients):
            for element in compound:
                if element not in atoms_count.keys():
                    atoms_count[element] = coeff * compound[element]
                else:
                    atoms_count[element] = atoms_count[element] + coeff * compound[element]
        return atoms_count

    def get_number_of_terms(self):
        return self.num_terms

    def __str__(self):
        string = ""
        for coeff, compound in zip(self.coefficients, self.compounds):
            term = "%d(" % coeff
            for element in compound:
                term = term + element + "_%d" % compound[element]
            term = term + ")"
            if string != "":
                string = string + " + " + term
            else:
                string = term
        return string

    def __iter__(self):
        self.terms_iter = iter(self.compounds)
        self.coeff_iter = iter(self.coefficients)
        return self

    def __next__(self):
        return self.coeff_iter.__next__(), self.terms_iter.__next__()


class Reactant(EquationSide):

    def isReactant(self):
        return True

    def isProduct(self):
        return False


class Product(EquationSide):
    def isProduct(self):
        return True

    def isReactant(self):
        return False


class ChemicalEquation:
    def __init__(self, reactants, products):
        self.reactants = reactants
        self.products = products
        self.number_terms = self.reactants.num_terms + self.products.num_terms

    def has_same_elements_in_both_sides(self):
        return set(self.reactants.get_list_of_elements()) == set(self.products.get_list_of_elements())

    def get_list_of_elements(self):
        elem_set = set()
        elem_set.update(self.products.get_list_of_elements())
        elem_set.update(self.reactants.get_list_of_elements())
        return list(elem_set)

    def isBalanced(self):
        if self.has_same_elements_in_both_sides():
            reactants_atoms_count = self.reactants.get_elements_atoms_count()
            product_atoms_count = self.products.get_elements_atoms_count()
            for element in self.get_list_of_elements():
                if reactants_atoms_count[element] != product_atoms_count[element]:
                    return False
            return True
        return False

    def balance(self):
        ### check if they have the same elements in both side... otherwise throw an error

        elements_involve = self.get_list_of_elements()
        sysEqu = [[1] + [0] * (self.number_terms - 1)] + [[0] * self.number_terms] * len(elements_involve)
        b = [1] + [0] * len(elements_involve)
        baseEqu = []
        # TODO: Considere coeff

        for element in elements_involve:
            curr_equ = []
            for compound in self.reactants.compounds:
                if compound.get(element):
                    curr_equ.append(compound[element])
                else:
                    curr_equ.append(0)
            for compound in self.products.compounds:
                if compound.get(element):
                    curr_equ.append(-1 * compound[element])
                else:
                    curr_equ.append(0)
            baseEqu.append(curr_equ)

        sysEqu[1:] = baseEqu
        A = Matrix(sysEqu)
        b = Matrix(b)
        solutions = list(linsolve((A, b)).args[0])
        # TODO: Raise an error if args is empty
        for i in range(self.number_terms):
            if solutions[i].q != 1:
                mult = solutions[i].q
                for j in range(self.number_terms):
                    solutions[j] = solutions[j] * mult
            if solutions[i].q == 1:
                solutions[i] = int(solutions[i])
        self.set_coefficients(solutions)

    def set_coefficients(self, new_coefficients):
        self.reactants.coefficients = new_coefficients[:self.reactants.num_terms]
        self.products.coefficients = new_coefficients[self.products.num_terms:]

    def __str__(self):
        return self.reactants.__str__() + " --> " + self.products.__str__()
