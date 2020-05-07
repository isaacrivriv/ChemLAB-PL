import operations

def printDetail(detailsDict):
    if isinstance(detailsDict, dict) and detailsDict.get("toDetail"):
        for element in detailsDict["details"]:
            print(element)
        return True
    else:
        return False


def buildDetailsDict(term, variables):
    details = {"toDetail": True, "details": []}
    varType = ""
    if type(term) is bool:
        varType = "Boolean"
    elif type(term) is int or type(term) is float:
        varType = "Number"
    else:
        varType = str(type(term))
    details['details'].append(varType + " ::= " + str(term))
    return details


def idLookUp(variables, id):
    return variables.get(id)


def manageTermOperation(firstTerm, operator, secondTerm):
    if operator == "*":
        return firstTerm * secondTerm
    elif operator == "/":
        return firstTerm / secondTerm
    elif operator == "+":
        return firstTerm + secondTerm
    elif operator == "-":
        return firstTerm - secondTerm
    elif operator == "!=":
        return firstTerm != secondTerm
    elif operator == "<=":
        return firstTerm <= secondTerm
    elif operator == ">=":
        return firstTerm >= secondTerm
    elif operator == ">":
        return firstTerm > secondTerm
    elif operator == "<":
        return firstTerm < secondTerm
    elif operator == ":=":
        return firstTerm == secondTerm
    elif operator == "&":
        # TODO: Need to fill this in with bond
        return operations.bond(firstTerm, secondTerm)
        # raise NotImplementedError("The & operator has not been implemented yet")
    elif operator == "|":
        # TODO: Need to fill this in with balance
        raise NotImplementedError("The | operator has not been implemented yet")
    else:
        # TODO: Need to fill this in with an appropriate error.
        raise NotImplementedError("The token was recognized as binoper but no oper implemented yet for " + operator)
