from tokens import Token, TokenType

LETTERS = 'abcdefghijklmnopqrstuvwxyz01234567890'

class Reader:
    def __init__(self, string: str):
        self.string = iter(string.replace(' ', '').replace('.', ''))
        self.input = set()
        self.Next()

    def Next(self):
        try:
            self.curr_char = next(self.string)
        except StopIteration:
            self.curr_char = None

    def CreateTokens(self):
        while self.curr_char is not None:
            if self.curr_char in LETTERS:
                self.input.add(self.curr_char)
                yield Token(TokenType.LETTER, self.curr_char)
                self.Next()

            elif self.curr_char in '*+':
                yield Token(TokenType.KLEENE if self.curr_char == '*' else TokenType.PLUS, self.curr_char)
                self.Next()

            elif self.curr_char == '|':
                yield Token(TokenType.OR, self.curr_char)
                self.Next()

            elif self.curr_char == '(':
                yield Token(TokenType.LPAR, self.curr_char)
                self.Next()

            elif self.curr_char == ')':
                yield Token(TokenType.RPAR, self.curr_char)
                self.Next()

            elif self.curr_char == '.':
                self.Next()
                if self.curr_char and self.curr_char in LETTERS + '(':
                    yield Token(TokenType.APPEND, '.')
                else:
                    raise Exception(f'Invalid input: {self.curr_char}')
            else:
                raise Exception(f'Invalid input: {self.curr_char}')

    def GetSymbols(self):
        return self.input

