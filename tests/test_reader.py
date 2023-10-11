
import sys
sys.path.append('../src')

import unittest
from tokens import Token, TokenType
from reader import Reader


class TestReader(unittest.TestCase):

    def test_token_creation(self):
        input_string = "(a|b)*"
        reader = Reader(input_string)
        expected_tokens = [
            Token(TokenType.LPAR, '(clear'),
            Token(TokenType.LETTER, 'a'),
            Token(TokenType.OR, '|'),
            Token(TokenType.LETTER, 'b'),
            Token(TokenType.RPAR, ')'),
            Token(TokenType.KLEENE, '*')
        ]

        tokens = list(reader.CreateTokens())

        self.assertEqual(tokens, expected_tokens)

    def test_get_symbols(self):
        input_string = "(a|b)*"
        reader = Reader(input_string)
        expected_symbols = {'a', 'b'}

        symbols = reader.GetSymbols()

        self.assertEqual(symbols, expected_symbols)

    def test_invalid_input(self):
        input_string = "(a|b)#"
        reader = Reader(input_string)

        with self.assertRaises(Exception):
            tokens = list(reader.CreateTokens())

if __name__ == '__main__':
    unittest.main()