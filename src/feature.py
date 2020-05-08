from chem_lex.ChemlabTokens import unit_prefix, supported_units
#import
from element import Element
def convertTo(el, num, Unit, newUnit):
    ### need to redo with the parser

    if(Unit in unit_prefix and Unit in unit_prefix):

        result = convertPrefix(num,Unit,newUnit)
        print("Result:    " + str(result)+" "+ newUnit)
    elif (Unit in supported_units and Unit in supported_units):

        result = convertUnit(el, num,Unit,newUnit)
        print("Result" + str(result)+" "+ newUnit)
    else:
        raise TypeError("Invalid Units is :  " + str(type(Unit)) )
    return result

def convertWeight(el ,num, Unit, newUnit):
    ### Converts weight related to an element
    if not isinstance(el, Element):
        raise TypeError("Not an element. Cannot perform operation")
    else:
        amu = el.dictionary['atomic_weight']
        if(Unit=='g'):
            if(newUnit=='mol'):
                result= num/amu
            elif(newUnit=='atoms'):
                mol = num/amu
                result = mol * (6.02*(10**23))
            else:
                raise TypeError("It's not possible to make that conversion")
        elif(Unit == 'mol'):
            if newUnit=='atoms':
                result = result = num*(6.02*(10**23))
            if newUnit=='g':
                result = num*amu
            else:
                raise TypeError("It's not possible to make that conversion")
        elif(Unit=='atoms'):
            if newUnit=='mol':
                result = num/(6.02*(10**23))
            if newUnit=='g':
                mol = num/(6.02*(10**23))
                result = mol * amu
            else:
                raise TypeError("It's not possible to make that conversion")
        else:
            raise TypeError("It's not possible to make that conversion")

    return result


pre = {'G': 10**9,  # GIGA
'M': 10**6,  # MEGA
'k': 10**3,  # KILO
'h': 10**2,  # HECTOR
'da': 10**1,  # DEKA
'd': 10**(-1),  # DECI
'c': 10**(-2),  # CENTI
'm': 10**(-3),  # MILLI
'u': 10**(-6),  # MICRO
'n': 10**(-9),  # NANO
'p': 10**(-12),  # PICO
'f': 10**(-15),
}
def convertPrefix(num,Unit,newUnit):
    CNum = num * pre[Unit]
    if (newUnit =='G'):
        result = CNum * (10**-9)
    if (newUnit=='M'):
        result = CNum * (10**-6)
    if (newUnit=='k'):
        result =CNum * (10**-3)
    if (newUnit=='h'):
        result = CNum * (10**-2)
    if (newUnit=='da'):
        result = CNum * (10**-1)

    if (newUnit=='d'):
        result = CNum * (10**(1))

    if (newUnit=='c'):
        result = CNum * (10**(2))

    if (newUnit=='m'):
        result = CNum * (10**(3))

    if (newUnit=='u'):
        result = CNum * (10**(6))

    if (newUnit=='n'):
        result = CNum * (10**(9))

    if (newUnit=='p'):
        result = CNum * (10**(12))

    if (newUnit=='f'):
        result = CNum * (10**(15))
    return result

Longitud = {'ft','me','mi'}
Weight = {'g','mol','atoms'}
Temp = {'K','C','F'}

def convertUnit(el, num , Unit,newUnit):
    if (Unit in Longitud):
        result = convertLong(num, Unit,newUnit)
    elif (Unit in Weight):
        result = convertWeight(el,num, Unit,newUnit)
    elif (Unit in Temp):
        result = convertTemp(num, Unit,newUnit)


    return result

def convertLong(num, Unit,newUnit):
    if (Unit == 'ft'):
        if (newUnit=='me'):
            result = num/3.2808
        elif newUnit=='mi':
            result = num/5280
        else:
            raise TypeError("It's not possible to make that conversion")
    elif Unit == 'me':
        if newUnit == 'ft':
            result = num*3.2808
        elif newUnit=='mi':
            result = num/1609
        else:
            raise TypeError("It's not possible to make that conversion")

    elif Unit == 'mi':
        if newUnit == 'ft':
            result = num*5280
        elif newUnit=='me':
            result = num*1609
        else:
            raise TypeError("It's not possible to make that conversion")
    else:
        raise TypeError("It's not possible to make that conversion")
    return result


def convertTemp(num, Unit, newUnit):
    if(Unit=='K'):
        if(newUnit=='C'):
            result = num - 273.15
        elif(newUnit=='F'):
            result = num * (9/5) - 459.67
        else:
            raise TypeError("It's not possible to make that conversion")
    elif(Unit=='C'):
        if(newUnit=='K'):
            result = num + 273.15
        elif(newUnit=='F'):
            result = (num * (9/5)) + 32
        else:
            raise TypeError("It's not possible to make that conversion")
    elif(Unit=='F'):
        if(newUnit=='C'):
            result = (num -32) * (5/9)
        elif(newUnit=='K'):
            result = (num +459.67 )*(5/9)
        else:
            raise TypeError("It's not possible to make that conversion")
    else:
        raise TypeError("It's not possible to make that conversion")
    return result
