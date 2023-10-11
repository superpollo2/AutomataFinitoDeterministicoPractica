from tokens import TokenType
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.next()

    def next(self):
        try:
            self.curr_token = next(self.tokens)
            print(self.curr_token)
        except StopIteration:
            self.curr_token = None

    def new_symbol(self):
        token = self.curr_token

        if token.type == TokenType.LPAR:
            self.next()
            res = self.expression()
            if self.curr_token.type != TokenType.RPAR:
                raise Exception('Sin paréntesis derecho para la expresión!')

            self.next()
            return res

        elif token.type == TokenType.LETTER:
            self.next()
            return Letter(token.value)

    def factor(self):
        res = self.new_symbol()

        while self.curr_token != None and \
                self.curr_token.type in (TokenType.KLEENE, TokenType.PLUS):
            if self.curr_token.type == TokenType.KLEENE:
                self.next()
                res = Kleene(res)
            elif self.curr_token.type == TokenType.PLUS:
                self.next()
                res = Plus(res)

        return res

    def term(self):
        res = self.factor()

        while self.curr_token != None and \
                self.curr_token.type == TokenType.APPEND:
            self.next()
            res = Append(res, self.factor())

        return res

    def expression(self):
        res = self.term()

        while self.curr_token != None and \
                self.curr_token.type == TokenType.OR:
            self.next()
            res = Or(res, self.term())

        return res

    def parse(self):
        if self.curr_token == None:
            return None

        res = self.expression()

        return res
