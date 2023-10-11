LETTERS = 'abcdefghijklmnopqrstuvwxyz0123456789'

errorList = []

class ValidExpresion:
    global errorList
    def __init__(self, string: str):
        print(string)
        self.string = iter(string.replace(' ', ''))
        self.curr_char = None
        self.Next()


    def Next(self):
        try:
            self.curr_char = next(self.string)
            print(self.curr_char)
        except StopIteration:
            self.curr_char = None


    def ntE(self):
        if (self.curr_char == '(' or self.curr_char in LETTERS):
            self.ntT()
            self.ntListaE()


    def ntListaE(self):
        if(self.curr_char == '|'):
            self.Next()
            self.ntT()
            self.ntListaE()


    def ntT(self):
        if (self.curr_char == '(' or self.curr_char in LETTERS):
            self.ntP()
            self.ntListaT()


    def ntListaT(self):
        if(self.curr_char == '.'):
            self.Next()
            self.ntP()
            self.ntListaT()


    def ntP(self):
        if (self.curr_char == '('):
            self.Next()
            self.ntE()
            if (self.curr_char == ')'):
                self.Next()
            else:
                errorList.append("Se esperaba un ')' después de una expresión.")
        elif (self.curr_char in LETTERS):
            self.Next()
            self.ntMod()
        else:
            errorList.append("Se esperaba un '(' o una letra o número.")


    def ntMod(self):
        if(self.curr_char == '*'):
            self.Next()
        elif(self.curr_char == '+'):
            self.Next()


    def listError(self):
        return errorList

def listError (self):
    return errorList
    



