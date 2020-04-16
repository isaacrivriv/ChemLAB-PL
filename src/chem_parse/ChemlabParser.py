import ply.yacc as yacc
import chem_lex.ChemlabTokens as toks
import re


class ChemlabParser:
    tokens = toks.tokens

    def p_exp_plus(self, p):
        '''ExpPlus :  Lbrack Exp Rbrack 
                        | Lbrack Exp Rbrack ExpPlus
        '''
        if self.trace:
            print("--ExpPlus: "+str(p[2]))
        if len(p) >4:
            p[0] = [p[2]] + p[4]
        else:
            p[0] = [p[2]]

    def p_exp(self, p):
        '''Exp : Term Binop Exp
                        | Term
                        | Def
                        | if Exp then Exp else Exp
                        | detail Lparen IdList Rparen'''
        # TODO: Fill logic here
        if self.trace:
            print("--Exp: "+str(p[1]))
        if p[1] == "detail":
            if p[3] is not None and p[3][0] is not None:
                for id in p[3]:
                    det = self.variables.get(id)
                    if det is None:
                        raise TypeError("Uninitialized Id passed for "+str(id))
                    print(det)
        else:
            p[0] = p[1]


    def p_term(self, p):
        '''Term : Sign Term
                        | Factor Lparen ExpList Rparen
                        | Factor
                        | Number
                        | Bool
                        | Empty'''
        # TODO: Fill logic here
        if self.trace:
            print("--Term: "+str(p[1]))
        if len(p)>4:
            if self.trace:
                print("Calling function for factor "+str(p[1]))
                print("with explist of "+str(p[3]))
            p[0] = 27
        elif isinstance(p[1],str) and re.match(r'\+|\-',p[1]): # If matches Sign
            if self.trace:
                print("Matched Sign")
                print(p[2])
            if p[1] == "-":
                p[0] = -1*p[2]
            else:
                p[0] = p[1]
        else:
            p[0] = p[1]


    def p_factor(self, p):
        '''Factor : Lparen Exp Rparen
                        | Prim
                        | Id'''
        # TODO: Fill logic here
        if self.trace:
            print("--Factor: "+str(p[1]))
        if p[1] == "(":
            p[0] = p[2]
        elif p[1] == "form":
            # Need to create something here
            p[0] = 23
        else: # It should be an id so fetch it from variables
            p[0] = self.variables.get(p[1])
            if p[0] is None:
                raise TypeError("Uninitialized Id passed for "+str(p[1]))

            


    def p_exp_list(self, p):
        '''ExpList : Empty
                        | PropExpList '''
        # TODO: Fill logic here
        if self.trace:
            print("--ExpList: "+str(p[1]))
            print(len(p))
        if len(p) < 2:
            if self.trace:
                print("Found none")
            pass
        else:
            p[0] = p[1]


    def p_prop_exp_list(self, p):
        '''PropExpList : Exp
                        | Exp Comma PropExpList'''
        # TODO: Fill logic here
        if self.trace:
            print("--PropExpList: "+str(p[1]))
        if len(p) < 3:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]


    def p_id_list(self, p):
        '''IdList : Empty
                        | PropIdList'''
        # TODO: Fill logic here
        if self.trace:
            print("--IdList: "+str(p[1]))
            print(len(p))
        if len(p) < 2:
            if self.trace:
                print("Found none")
            pass
        else:
            p[0] = p[1]


    def p_prop_id_list(self, p):
        '''PropIdList : Id
                        | Id Comma PropIdList'''
        # TODO: Fill logic here
        if self.trace:
            print("--PropIdList: "+str(p[1]))
        if len(p) < 3:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]


    def p_def(self, p):
        '''Def : Id Equal Exp Semicolon'''
        # TODO: Fill logic here
        if self.trace:
            print("--Def: "+str(p[1]))
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
        # TODO: Fill logic here
        if self.trace:
            print("--Bool: "+str(p[1]))
        if p[1] == "TRUE":
            p[0] = True
        else:
            p[0] = False


    def p_sign(self, p):
        '''Sign : Plus
                        | Minus'''
        # TODO: Fill logic here
        if self.trace:
            print("--Sign: "+str(p[1]))
        p[0] = p[1]


    def p_binop(self, p):
        '''Binop : Sign
                        | Binoper'''
        # TODO: Fill logic here
        if self.trace:
            print("--Binop: "+str(p[1]))


    def p_prim(self, p):
        '''Prim : Primtok'''
        if self.trace:
            print("--Prim: "+str(p[1]))
        p[0] = p[1]
        # TODO: Fill logic here


    def p_id(self, p):
        '''Id : Idtok'''
        # TODO: Fill logic here
        if self.trace:
            print("--Id: "+str(p[1]))
        p[0] = p[1]


    def p_int(self, p):
        '''Number : Integer
                  | Float'''
        # TODO: Fill logic here
        if self.trace:
            print("--Number: "+str(p[1]))
        p[0] = p[1]


    def p_error(self, p):
        raise TypeError("Syntax error found parsing "+str(p))

    # Build the parser
    def build(self, trace=False, **kwargs):
        self.variables = {}
        self.trace = trace
        self.parser = yacc.yacc(module=self)

    def parseContent(self, content, lexer):
        self.parser.parse(content, lexer=lexer)
