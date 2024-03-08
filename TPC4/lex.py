import ply.lex as lex
import re

tokens = [
    'SELECT',
    'FROM',
    'WHERE',
    'IDENTIFIER',
    'NUMBER',
    'COMPARISON',
    'COMMA',
]

def t_SELECT(t):
    r'SELECT'
    return t

def t_FROM(t):
    r'FROM'
    return t

def t_WHERE(t):
    r'WHERE'
    return t

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_COMPARISON = r'[<>]=?|='
t_COMMA = r','
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex(reflags=re.IGNORECASE)

data = 'Select id, nome, salario From empregados Where salario >= 820'
lexer.input(data)
while True:
    token = lexer.token()
    if not token:
        break
    print(token)
