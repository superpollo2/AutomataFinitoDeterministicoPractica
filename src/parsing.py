from tokens import TokenType
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.Next()

    def Next(self):
        try:
            self.curr_token = next(self.tokens)
            print(self.curr_token)
        except StopIteration:
            self.curr_token = None

    def NewSymbol(self):
        token = self.curr_token

        if token.type == TokenType.LPAR:
            self.Next()
            res = self.Expression()
            if self.curr_token.type != TokenType.RPAR:
                raise Exception('Sin paréntesis derecho para la expresión!')

            self.Next()
            return res

        elif token.type == TokenType.LETTER:
            self.Next()
            return Letter(token.value)

    def Factor(self):
        res = self.NewSymbol()

        while self.curr_token != None and \
                self.curr_token.type in (TokenType.KLEENE, TokenType.PLUS):
            if self.curr_token.type == TokenType.KLEENE:
                self.Next()
                res = Kleene(res)
            elif self.curr_token.type == TokenType.PLUS:
                self.Next()
                res = Plus(res)

        return res

    def Term(self):
        res = self.Factor()

        while self.curr_token != None and \
                self.curr_token.type == TokenType.APPEND:
            self.Next()
            res = Append(res, self.Factor())

        return res

    def Expression(self):
        res = self.Term()

        while self.curr_token != None and \
                self.curr_token.type == TokenType.OR:
            self.Next()
            res = Or(res, self.Term())

        return res

    def Parse(self):
        if self.curr_token == None:
            return None

        res = self.Expression()

        return res
