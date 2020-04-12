reserved = {
    'if': 'if',
    'else': 'else',
    'then': 'then',
    'TRUE': 'TRUE',
    'FALSE': 'FALSE',
    'detail': 'detail'
}

tokens = [
    'Number',
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
    'Primtok',
    'Comment',
    ] + list(reserved.values())