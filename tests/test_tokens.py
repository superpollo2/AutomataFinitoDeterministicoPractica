import unittest
from enum import Enum



class TokenType(Enum):
    LETTER = 0
    APPEND = 1
    OR = 2
    KLEENE = 3
    PLUS = 4
    LPAR = 6
    RPAR = 7


class Token:
    def __init__(self, type: TokenType, value=None):
        self.type = type
        self.value = value
        self.precedence = type.value

    def __repr__(self):
        return f'{self.type.name}: {self.value}'

class TestToken(unittest.TestCase):

    def test_token_creation(self):
        token = Token(TokenType.LETTER, 'a')
        self.assertEqual(token.type, TokenType.LETTER)
        self.assertEqual(token.value, 'a')
        self.assertEqual(token.precedence, TokenType.LETTER.value)

    def test_token_representation(self):
        token = Token(TokenType.APPEND, None)
        self.assertEqual(repr(token), 'APPEND: None')

if __name__ == '__main__':
    unittest.main()
