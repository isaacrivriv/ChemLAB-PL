import ply.yacc as yacc
import src.chem_lex.ChemlabTokens as toks
import src.chem_parse.ParsingUtils as utils
import re


class ChemlabParser:
    tokens = toks.tokens
    precedence = toks.precedence

    def p_exp_plus(self, p):
        '''ExpPlus :  Lbrack Exp Rbrack 
                        | Lbrack Exp Rbrack ExpPlus
        '''
        if self.trace:
            print("--ExpPlus: " + str(p[2]))
        if len(p) > 4:
            p[0] = [p[2]] + p[4]
        else:
            p[0] = [p[2]]
        self.inIntermediateState = 0  # Reset intermediate state in case something went wrong

    def p_exp(self, p):
        '''Exp : Term
                        | Def
                        | detail Lparen Printable Rparen
                        | if goToIntermediate Exp then Exp else Exp'''
        if self.trace:
            print("--Exp: " + str(p[1]))
        if p[1] == "if":  # Manage if else logic
            if self.trace:
                print("----Running if: " + str(p[3]))
            if not isinstance(p[3], bool):
                raise TypeError("Invalid boolean argument passed to if statement")
            if p[3]:
                if self.trace:
                    print("----Running then expression: " + str(p[5]))
                utils.printDetail(p[5])
                # TODO: Fill out what to call here if necessary
                p[0] = p[5]
            else:
                if self.trace:
                    print("----Running else expression: " + str(p[7]))
                utils.printDetail(p[7])
                # TODO: Fill out what to call here if necessary
                p[0] = p[7]
            self.inIntermediateState -= 1
        elif p[
            1] == "detail":  # Manage printing and detail function logic. Might be better to move this to a utils class
            if self.inIntermediateState > 0:
                p[0] = p[3]
            else:
                utils.printDetail(p[3])
        else:
            # If its a Def or just a term alone we just pass it along the expression
            p[0] = p[1]

    def p_in_intermeddiate(self, p):
        '''goToIntermediate :'''
        self.inIntermediateState += 1  # Set in intermeddiate to not print code when calling detail with if

    def p_printable(self, p):
        '''Printable : Term
                        | Term Comma Printable'''
        if self.trace:
            print("--Printable: " + str(p[1]))
        p[0] = utils.buildDetailsDict(p[1], self.variables)

        if len(p) > 2:  # We need to concatenate the other detail list if it appears as a comma separated value
            p[0]['details'] = p[0]['details'] + p[3]['details']

    def p_term(self, p):
        '''Term : Sign Term
                        | Term Plus Term
                        | Term Minus Term
                        | Term Multiplication Term
                        | Term Division Term
                        | Term Bond Term
                        | Term Balance Term
                        | Term Binoper Term
                        | Factor Lparen ExpList Rparen
                        | Factor
                        | Number
                        | Bool'''
        if self.trace:
            print("--Term: " + str(p[1]))
        if len(p) > 4:
            if self.trace:
                print("----Calling function for factor " + str(p[1]))
                print("----with explist of " + str(p[3]))
            p[0] = 34  # TODO: Placeholder code to call functions if we can push it in
        elif len(p) > 3:  # Identified a term with an operation so manage it acordingly
            if self.trace:
                print("----Located Term: " + str(p[1]))
                print("----Found Binop: " + str(p[2]))
                print("----Applied to exp: " + str(p[3]))
            p[0] = utils.manageTermOperation(p[1], p[2], p[3])
            if self.trace:
                print("----Returning Term: " + str(p[0]))
        elif len(p) > 2:  # If matches Sign at beggining
            if self.trace:
                print("----Matched Sign: " + str(p[1]))
            if p[1] == "-":
                p[0] = -1 * p[2]
            else:
                p[0] = p[2]
        else:  # We found either a Factor, Number or Bool at this point so just pass it along
            p[0] = p[1]

    def p_factor(self, p):
        '''Factor : Lparen Exp Rparen
                        | Builtin
                        | Id'''
        # TODO: Fill logic here
        if self.trace:
            print("--Factor: " + str(p[1]))
        if p[1] == "(":
            p[0] = p[2]
        elif type(p[1]) is str:  # It should be an id so fetch it from variables
            p[0] = self.variables.get(p[1])
            if p[0] is None:
                raise TypeError("Uninitialized Id passed for " + str(p[1]))
        else:  # Check if the factor is a built in function and pass the appropriate value
            p[0] = p[1]["value"]

    def p_built_in(self, p):
        '''Builtin : convert Lparen Id checkIdIsElem Comma Number Comma Unit Comma Unit Rparen
                        | convert Lparen FormFunc Comma Number Comma Unit Comma Unit Rparen
                        | FormFunc
                        | isBalanced Lparen ElemList Rparen'''
        if self.trace:
            print("--Builtin: " + str(p[1]))
        # TODO: Probably do a lookup of a util function that matches what was passed and pass the result along the tree
        # TODO: Placeholder code. Need to fill this with the proper calls
        p[0] = {"function": p[1], "value": None}
        if p[1] == "convert":
            if self.trace:
                if p[4] == ',':
                    print("----convert: " + str(p[3]) + " ; value: " + str(p[5]) + " from: " + str(
                        p[7]) + " ; to: " + str(p[9]))
                else:
                    print("----convert: " + str(p[3]) + " ; value: " + str(p[6]) + " from: " + str(
                        p[8]) + " ; to: " + str(p[10]))
            p[0]["value"] = 24.6
        elif p[1] == "balanced?":
            if self.trace:
                print("----balanced?: " + str(p[3]))
            p[0]["value"] = True
        else:
            if self.trace:
                print("----form: " + str(p[1]))
            p[0]["value"] = p[1]

    def p_form_manage(self, p):
        '''FormFunc : form Lparen Id checkIdIsInteger Rparen
                        | form Lparen Integer Rparen'''
        # TODO: Probably do a lookup of a util function that matches what was passed and pass the result along the tree
        # TODO: Placeholder code. Need to fill this with the proper calls
        if self.trace:
            print("--FormFunc: " + str(p[3]))
        p[0] = 27

    def p_unit(self, p):
        '''Unit : UnitTok
                        | PrefixTok Unit'''
        # TODO: Maybe a lookup is necessary here? Need to check whats the best way to implement this.
        # Language allows for this to have prefixes and prefixes and so on so on so we need to think on how to implement this
        if self.trace:
            print("--Unit")
        if type(p[1]) is not tuple:
            p[1] = tuple([p[1]])
        if len(p) > 2:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]
        if self.trace:
            print("----Val: " + str(p[0]))

    def p_is_elem(self, p):
        '''checkIdIsElem :'''
        # TODO: Verify if id passed is an element or compound (p[-1] to get the id)
        # TODO: Placeholder code. Need to fill this with the proper code
        if self.trace:
            print("--checkIdIsElem")
        p[0] = True

    def p_is_integer(self, p):
        '''checkIdIsInteger :'''
        # Verify if id passed is an integer (p[-1] to get the id)
        if self.trace:
            print("--checkIdIsInteger")
        var = self.variables.get(p[-1])
        if var is None:
            raise TypeError("Uninitialized Id passed for " + str(p[-1]))
        else:
            return type(var) is int

    def p_elem_list(self, p):  # TODO: For now this is just an id list but need to check if we need to add more
        '''ElemList : Id checkIdIsElem
                        | Id checkIdIsElem Comma ElemList'''
        if self.trace:
            print("--ElemList")
        if p[2]:
            p[0] = self.variables.get(p[1])
            if p[0] is None:
                raise TypeError("Uninitialized Id passed for " + str(p[1]))
            p[0] = [p[0]]
            if len(p) > 3:
                p[0] = p[0] + p[4]
        else:
            raise TypeError("Invalid argument passed: " + str(p[1]))

    def p_exp_list(self, p):
        '''ExpList : Empty
                        | PropExpList '''
        if self.trace:
            print("--ExpList: " + str(p[1]))
            print("----Length: " + str(len(p)))
        if len(p) < 2:
            if self.trace:
                print("----Found none")
            pass
        else:
            p[0] = p[1]

    def p_prop_exp_list(self, p):
        '''PropExpList : Exp
                        | Exp Comma PropExpList'''
        if self.trace:
            print("--PropExpList: " + str(p[1]))
        if len(p) < 3:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_def(self, p):
        '''Def : Id Equal Exp Semicolon'''
        if self.trace:
            print("--Def: " + str(p[1]))
        # Def initializes a variable in the variables dictionary and also passes the Exp part along as an expression
        self.variables[p[1]] = p[3]
        p[0] = p[3]

    def p_empty(self, p):
        '''Empty :'''
        if self.trace:
            print("--Empty: ")
        pass

    def p_bool(self, p):
        '''Bool : TRUE
                        | FALSE'''
        if self.trace:
            print("--Bool: " + str(p[1]))
        if p[1] == "TRUE":
            p[0] = True
        else:
            p[0] = False

    def p_sign(self, p):
        '''Sign : Plus
                        | Minus'''
        if self.trace:
            print("--Sign: " + str(p[1]))
        p[0] = p[1]

    def p_id(self, p):
        '''Id : Idtok'''
        if self.trace:
            print("--Id: " + str(p[1]))
        p[0] = p[1]

    def p_number(self, p):
        '''Number : Integer
                  | Float'''
        if self.trace:
            print("--Number: " + str(p[1]))
        p[0] = p[1]

    def p_error(self, p):
        raise TypeError("Syntax error found parsing " + str(p))

    # Build the parser
    def build(self, trace=False, **kwargs):
        self.variables = {}
        self.trace = trace
        self.parser = yacc.yacc(module=self)
        self.inIntermediateState = 0

    def parseContent(self, content, lexer):
        self.parser.parse(content, lexer=lexer)
