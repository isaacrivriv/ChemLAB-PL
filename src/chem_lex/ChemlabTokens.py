reserved = {
    'if': 'if',
    'else': 'else',
    'then': 'then',
    'TRUE': 'TRUE',
    'FALSE': 'FALSE',
    'detail': 'detail',
    'convert': 'convert',
    'form': 'form',
    'balanced?': 'isBalanced',
    'balance': 'balance',
}

unit_prefix = {
    'G': 'PrefixTok',  # GIGA
    'M': 'PrefixTok',  # MEGA
    'k': 'PrefixTok',  # KILO
    'h': 'PrefixTok',  # HECTOR
    'da': 'PrefixTok',  # DEKA
    'd': 'PrefixTok',  # DECI
    'c': 'PrefixTok',  # CENTI
    'm': 'PrefixTok',  # MILLI
    'u': 'PrefixTok',  # MICRO
    'n': 'PrefixTok',  # NANO
    'p': 'PrefixTok',  # PICO
    'f': 'PrefixTok',  # FEMTO
}

supported_units = {
    'ft': 'UnitTok',  # FEET
    'me': 'UnitTok',  # METERS
    'g': 'UnitTok',  # GRAMS
    's': 'UnitTok',  # SECONDS
    'mi': 'UnitTok',  # MILES
    'K': 'UnitTok',  # KELVIN
    'C': 'UnitTok',  # CELSIUS
    'F': 'UnitTok',  # FARENHEIT
    'mol': 'UnitTok',  # MOL
    'atoms': 'UnitTok',  # ATOMS
    'L': 'UnitTok',  # LITERS
    # OPTIONAL TO IMPLEMENT
    'A': 'UnitTok',  # AMPERE
    'cd': 'UnitTok',  # CANDELA
}


tokens = [
             'Integer',
             'Float',
             'Idtok',
             'Lparen',
             'Rparen',
             'Lbrack',
             'Rbrack',
             'Semicolon',
             'Comma',
             'Binoper',
             'Equal',
             'Plus',
             'Minus',
             'Multiplication',
             'Division',
             'Bond',
             'Comment',
             'UnitTok',
             'PrefixTok',
             'Separator'
         ] + list(reserved.values())

precedence = (
    ('nonassoc', 'Binoper'),  # Nonassociative operators
    ('left', 'Plus', 'Minus'),
    ('left', 'Multiplication', 'Division'),
    ('left', 'Bond'),
)
