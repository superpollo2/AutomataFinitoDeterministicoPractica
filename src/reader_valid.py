LETTERS = 'abcdefghijklmnopqrstuvwxyz0123456789'

error_list = []

class ValidExpresion:
    global error_list
    def __init__(self, string: str):
        print(string)
        self.string = iter(string.replace(' ', ''))
        self.curr_char = None
        self.next()


    def next(self):
        try:
            self.curr_char = next(self.string)
            print(self.curr_char)
        except StopIteration:
            self.curr_char = None


    def nt_e(self):
        if (self.curr_char == '(' or self.curr_char in LETTERS):
            self.nt_t()
            self.nt_lista_e()


    def nt_lista_e(self):
        if(self.curr_char == '|'):
            self.next()
            self.nt_t()
            self.nt_lista_e()


    def nt_t(self):
        if (self.curr_char == '(' or self.curr_char in LETTERS):
            self.nt_p()
            self.nt_lista_t()


    def nt_lista_t(self):
        if(self.curr_char == '.'):
            self.next()
            self.nt_p()
            self.nt_lista_t()


    def nt_p(self):
        if (self.curr_char == '('):
            self.next()
            self.nt_e()
            if (self.curr_char == ')'):
                self.next()
            else:
                error_list.append("Se esperaba un ')' después de una expresión.")
        elif (self.curr_char in LETTERS):
            self.next()
            self.nt_mod()
        else:
            error_list.append("Se esperaba un '(' o una letra o número.")


    def nt_mod(self):
        if self.curr_char == '*' or self.curr_char == '+':
            self.next()
        

    def list_error(self):
        return error_list


    



