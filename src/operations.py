import math
from element import Element
from Compound import Compound


def bond(e1, e2):
    if not isinstance(e1, Element):
        try:
            e1 = Element(e1)
        except TypeError:
            print("First item is not an element")
    if not isinstance(e2, Element):
        try:
            e2 = Element(e2)
        except TypeError:
            print("Second item is not an element")

    e1_charge = abs(charge(e1))
    e2_charge = abs(charge(e2))
    gcd = math.gcd(e1_charge, e2_charge)    # greatest common denominator
    e1_charge = e1_charge // gcd
    e2_charge = e2_charge // gcd

    if (e1.dictionary['type'] == 'Non Metal' and e2.dictionary['type'] == 'Non Metal') \
            and (abs(e1.dictionary['electronegativity'] - e2.dictionary['electronegativity']) < 2):
        return Compound({e1: e2_charge, e2: e1_charge}, 'covalent')
    elif (e1.dictionary['type'] == 'Metal' and e2.dictionary['type'] == 'Non Metal') \
            or (e1.dictionary['type'] == 'Non Metal' and e2.dictionary['type'] == 'Metal'):
        return Compound({e1: e2_charge, e2: e1_charge}, 'ionic')
    elif e1.dictionary['type'] == 'Metal' and e2.dictionary['type'] == 'Metal':
        return Compound({e1: e2_charge, e2: e1_charge}, 'metallic')
    else:
        return Compound({e1: e2_charge, e2: e1_charge}, None)


# determine the electric charge of an element from its group (used for determining bond subscripts)
def charge(e):
    if e.dictionary['atomic_num'] == 6:     # C
        return 4
    elif e.dictionary['atomic_num'] == 47:  # Ag
        return 3
    elif e.dictionary['atomic_num'] in (13, 31):  # Al or Ga
        return 3
    elif e.dictionary['atomic_num'] in (30, 48):  # Zn or Cd
        return 2
    elif e.dictionary['group'] in (1, 2):
        return e.dictionary['group']
    elif e.dictionary['group'] in (15, 16, 17, 18) and e.dictionary['type'] == 'Non Metal':
        return e.dictionary['group'] - 18
    else:
        # TODO: figure out what to do with transition metals, their charge varies
        return 1
