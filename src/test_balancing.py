from src.ChemicalEquation import Reactant, Product, ChemicalEquation
from src.Compound import Compound
from src.element import Element



def main():
    # r = Reactant((Compound({Element('1'): 1}), Compound({Element('8'): 1})))
    # p = Product({Element('1'): 2, Element('8'): 1})
    # chem_equ = ChemicalEquation(r, p)
    # print(f"Before Balancing isBalanced() = {chem_equ.isBalanced()}")
    # chem_equ.balance()
    # print(chem_equ)
    # print(f"After Balancing isBalanced() = {chem_equ.isBalanced()}")
    # print("")

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
    He = Element('2')
    H = Element('1')
    print(He.full_detail_str())
    c = Compound({He: 1, H: 3})
    print(c)


if __name__ == "__main__":
    main()
