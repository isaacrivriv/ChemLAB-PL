import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/valericita/Documents/GitHub/ChemLAB-PL/src/chem_lex')

import ChemlabTokens
import Element from element
def convertTo(num, Unit, newUnit):
    ### need to redo with the parser
    if(Unit in ChemlabTokens.unit_prefix and newUnit in ChemlabTokens.unit_prefix):
        result = convertPrefix(num,Unit,newUnit)
    if(Unit in ChemlabTokens.supported_units and newUnit in ChemlabTokens.supported_units):
        result = convertUnit(num,Unit,newUnit)

    return result

def convertTo(el ,num, Unit, newUnit):
    ### Converts weight related to an element
    if not isinstance(el, Element):
        raise TypeError("Not an element. Cannot perform operation")
    else:
        amu = el.dictionary['atomic_weight']
        elif(Unit=='g'):
            if(newUnit=='mol'):

            elif(newUnit=='atoms'):
                mol = num/amu
                result = mol * (6.02*(10**23))
        elif(Unit == 'mol'):
        elif(Unit=='atoms'):
        else:
            raise TypeError("It's not possible to make that conversion")

    return result


def convertPrefix(num,Unit,newUnit):
    if (newUnit =='G'):
        result = num * (10**9)
    if (newUnit=='M'):
        result = num * (10**6)
    if (newUnit=='k'):
        result = num * (10**3)
    if (newUnit=='h'):
        result = num * (10**2)
    if (newUnit=='da'):
        result = num * (10**1)

    if (newUnit=='d'):
        result = num * (10**(-1))

    if (newUnit=='c'):
        result = num * (10**(-2))

    if (newUnit=='m'):
        result = num * (10**(-3))

    if (newUnit=='u'):
        result = num * (10**(-6))

    if (newUnit=='n'):
        result = num * (10**(-9))

    if (newUnit=='p'):
        result = num * (10**(-12))

    if (newUnit=='f'):
        result = num * (10**(-15))
    return result

Longitud = {'ft','me','mi'}
Weight = {'g','mol','atoms'}
Temp = {'K','C','F'}

def convertUnit(num,Unit,newUnit):
    if (Unit in Longitud):
        result = convertLong(num, Unit,newUnit)
    elif (Unit in Weight):
        result = convertWeight(num, Unit,newUnit)
    elif (Unit in Temp):
        result = convertTemp(num, Unit,newUnit)


    return result

def convertLong(num, Unit,newUnit):
    if (Unit == 'ft'):
        if (newUnit=='me'):
            result = num/3.2808
        elif newUnit=='mi':
            result = num/5280
    elif Unit == 'me':
        if newUnit == 'ft':
            result = num*3.2808
        elif newUnit=='mi':
            result = num/1609

    elif Unit == 'mi':
        if newUnit == 'ft':
            result = num*5280
        elif newUnit=='me':
            result = num*1609
    else:
        raise TypeError("It's not possible to make that conversion")
    return result


def convertTemp(num, Unit, newUnit):
    if(Unit=='K'):
        if(newUnit=='C'):
            result = num - 273.15
        elif(newUnit=='F'):
            result = num * (9/5) - 459.67
    elif(Unit=='C'):
        if(newUnit=='K'):
            result = num + 273.15
        elif(newUnit=='F'):
            result = (num * (9/5)) + 32
    elif(Unit=='F'):
        if(newUnit=='C'):
            result = (num -32) * (5/9)
        elif(newUnit=='K'):
            result = (num +459.67 )*(5/9)
    else:
        raise TypeError("It's not possible to make that conversion")
    return result



##test
print("result =   " + str(convertTo(1,'mi','ft')))
