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
        while self.curr_char != None:

            if self.curr_char in LETTERS:
                self.input.add(self.curr_char)
                yield Token(TokenType.LETTER, self.curr_char)
                
                self.next()

                # para finalizar, se verifica si necesitamos agregar un token append
                if self.curr_char != None and \
                        (self.curr_char in LETTERS or self.curr_char == '('):
                    yield Token(TokenType.APPEND, '.')

            elif self.curr_char == '|':
                yield Token(TokenType.OR, '|')

                self.next()

                if self.curr_char != None and self.curr_char not in '()':
                    yield Token(TokenType.LPAR)

                    while self.curr_char != None and self.curr_char not in ')*+':
                        if self.curr_char in LETTERS:
                            self.input.add(self.curr_char)
                            yield Token(TokenType.LETTER, self.curr_char)

                            self.next()
                            if self.curr_char != None and \
                                    (self.curr_char in LETTERS or self.curr_char == '('):
                                yield Token(TokenType.APPEND, '.')

                    if self.curr_char != None and self.curr_char in '*+':
                        self.rparPending = True
                    elif self.curr_char != None and self.curr_char == ')':
                        yield Token(TokenType.RPAR, ')')
                    else:
                        yield Token(TokenType.RPAR, ')')

            elif self.curr_char == '(':
                self.next()
                yield Token(TokenType.LPAR)

            elif self.curr_char in (')*+'):

                if self.curr_char == ')':
                    self.next()
                    yield Token(TokenType.RPAR)

                elif self.curr_char == '*':
                    self.next()
                    yield Token(TokenType.KLEENE)

                elif self.curr_char == '+':
                    self.next()
                    yield Token(TokenType.PLUS)


                if self.rparPending:
                    yield Token(TokenType.RPAR)
                    self.rparPending = False

                #para finalizar, se verifica si necesitamos agregar un token append
                if self.curr_char != None and \
                        (self.curr_char in LETTERS or self.curr_char == '('):
                    yield Token(TokenType.APPEND, '.')

            else:
                raise Exception(f'Invalid entry: {self.curr_char}')

        yield Token(TokenType.APPEND, '.')
        yield Token(TokenType.LETTER, '#')

    def get_symbols(self):
        return self.input
