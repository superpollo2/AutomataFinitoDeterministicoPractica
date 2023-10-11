from tokens import Token, TokenType
from parsing import UnknownOperatorError
LETTERS = 'abcdefghijklmnopqrstuvwxyz01234567890'

class Reader:
    def __init__(self, string: str):
        self.string = iter(string.replace(' ', '').replace('.', ''))
        self.input = set()
        self.next()

    def next(self):
        try:
            self.curr_char = next(self.string)
        except StopIteration:
            self.curr_char = None

    def create_tokens(self):
        while self.curr_char is not None:
            if self.curr_char in LETTERS:
                self.input.add(self.curr_char)
                yield Token(TokenType.LETTER, self.curr_char)
                self.next()

            elif self.curr_char in '*+':
                yield Token(TokenType.KLEENE if self.curr_char == '*' else TokenType.PLUS, self.curr_char)
                self.next()

            elif self.curr_char == '|':
                yield Token(TokenType.OR, self.curr_char)
                self.next()

            elif self.curr_char == '(':
                yield Token(TokenType.RPAR, self.curr_char)
                self.next()

            elif self.curr_char == ')':
                yield Token(TokenType.LPAR, self.curr_char)
                self.next()

            elif self.curr_char == '.':
                self.next()
                if self.curr_char and self.curr_char in LETTERS + '(':
                    yield Token(TokenType.APPEND, '.')
                else:
                    raise UnknownOperatorError(self.curr_char)
            else:
                raise UnknownOperatorError(self.curr_char)

    def get_symbols(self):
        return self.input

