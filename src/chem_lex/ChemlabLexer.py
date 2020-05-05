import ply.lex as lex
import chem_lex.ChemlabTokens as toks


class ChemLABLexer:
    tokens = toks.tokens

    t_Lparen = r'\('
    t_Rparen = r'\)'
    t_Lbrack = r'\['
    t_Rbrack = r'\]'
    t_Comma = r','
    t_Semicolon = r';'
    t_Binoper = r':=|!=|<=|>=|<|>'
    t_Equal = r'='
    t_Plus = r'\+'
    t_Minus = r'\-'
    t_Multiplication = r'\*'
    t_Division = r'\/'
    t_Bond = r'&'
    t_Balance = r'\|'
    t_Separator = r'\->'

    def t_Float(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_Integer(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_Idtok(self, t):  # Identifies units and prefixes as well
        r'[A-Za-z\?_][A-Za-z0-9\?_]*'
        reservedTokens = dict(toks.reserved, **(toks.supported_units))
        reservedTokens.update(toks.unit_prefix)
        reservedTokens.update(toks.combination_unit_prefix)
        t.type = reservedTokens.get(t.value, 'Idtok')
        if type(t.type) is tuple:
            t.value = t.type
            t.type = 'UnitTok'
        return t

    def t_Comment(self, t):
        r'\^\^.*'
        pass

    # Ignored characters whitespace and tabs
    t_ignore = " \t"

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        raise TypeError("Illegal character found scanning '%s'" % t.value[0])

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: break
            print(tok)
