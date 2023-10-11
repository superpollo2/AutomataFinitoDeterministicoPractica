from enum import Enum


class TokenType(Enum):
    LETTER = 0
    APPEND = 1
    OR = 2
    KLEENE = 3
    PLUS = 4
    RPAR = 6
    LPAR = 7


class Token:
    def __init__(self, type: TokenType, value=None):
        self.type = type
        self.value = value
        self.precedence = type.value

    def __repr__(self):
        return f'{self.type.name}: {self.value}'
