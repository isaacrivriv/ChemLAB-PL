from ChemicalEquation import Reactant, Product, ChemicalEquation
from Compound import Compound
from element import Element


def main():
    r = Reactant(({'P': 1, 'Cl': 5}, {'H': 2, 'O': 1}))
    p = Product(({'H': 3, 'P': 1, 'O': 4}, {'H': 1, 'Cl': 1}))

    chem_equ_2 = ChemicalEquation(r, p)
    print(f"Before Balancing isBalanced() = {chem_equ_2.isBalanced()}")
    chem_equ_2.balance()
    print(chem_equ_2)
    print(f"After Balancing isBalanced() = {chem_equ_2.isBalanced()}")
    print("")

    r = Reactant(({'Fe': 2, 'O': 3}, {'C': 1}))
    p = Product(({'Fe': 1}, {'C': 1, 'O': 2}))

    chem_equ_3 = ChemicalEquation(r, p)
    print(f"Before Balancing isBalanced() = {chem_equ_3.isBalanced()}")
    chem_equ_3.balance()
    print(chem_equ_3)
    print(f"After Balancing isBalanced() = {chem_equ_3.isBalanced()}")
    print("Done")


if __name__ == "__main__":
    main()
