import sys
sys.path.append('../src')

import unittest
from tokens import Token, TokenType  
from direct_reader import DirectReader  



class TestDirectReader(unittest.TestCase):
    def test_create_tokens(self):
        input_string = "a|b.(c*+d)"
        reader = DirectReader(input_string)
        tokens = list(reader.CreateTokens())

        expected_tokens = [
            Token(TokenType.LETTER, 'a'),
            Token(TokenType.OR, '|'),
            Token(TokenType.LETTER, 'b'),
            Token(TokenType.APPEND, '.'),
            Token(TokenType.LPAR, '('),
            Token(TokenType.LETTER, 'c'),
            Token(TokenType.KLEENE, '*'),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.LETTER, 'd'),
            Token(TokenType.RPAR, ')'),
            Token(TokenType.APPEND, '.'),
            Token(TokenType.LETTER, '#')
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_get_symbols(self):
        input_string = "a|b.(c*+d)"
        reader = DirectReader(input_string)
        reader.CreateTokens()
        symbols = reader.GetSymbols()

        expected_symbols = {'a', 'b', 'c', 'd'}

        self.assertEqual(symbols, expected_symbols)

if __name__ == '__main__':
    unittest.main()
