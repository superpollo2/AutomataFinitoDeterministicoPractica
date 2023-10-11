from tokens import Token, TokenType

LETTERS = 'abcdefghijklmnopqrstuvwxyz01234567890.'


class DirectReader:

    def __init__(self, string: str):
        self.string = iter(string.replace(' ', ''))
        self.string = iter(string.replace('.',''))
        self.input = set()
        self.rparPending = False
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
            elif self.curr_char in '()':
                yield self.handle_parentheses()
            elif self.curr_char == '|':
                yield Token(TokenType.OR, '|')
                self.next()
            elif self.curr_char in '*+':
                yield self.handle_repetitions()
            else:
                raise Exception(f'Invalid entry: {self.curr_char}')

        yield Token(TokenType.APPEND, '.')
        yield Token(TokenType.LETTER, '#')

    def handle_parentheses(self):
        if self.curr_char == '(':
            self.next()
            return Token(TokenType.LPAR)
        elif self.curr_char == ')':
            self.next()
            return Token(TokenType.RPAR)
        else:
            raise Exception(f'Invalid entry inside parentheses: {self.curr_char}')

    def handle_repetitions(self):
        token_type = TokenType.KLEENE if self.curr_char == '*' else TokenType.PLUS
        self.next()
        return Token(token_type)



    def get_symbols(self):
        return self.input
