LETTERS = 'abcdefghijklmnopqrstuvwxyz01234567890'

errorList = []
x = ''
class ValidExpresion:
    global errorList
    def __init__(self, string: str):
        print(string)
        self.string = iter(string.replace(' ', ''))
        self.input = set()
        self.rparPending = False
        self.Next()


    def Next(self):
        global x
        try:
            
            self.curr_char = next(self.string)
            print(self.curr_char)
        except StopIteration:
            self.curr_char = None


    def ntE(self):
        if (self.curr_char == '(' or self.curr_char in LETTERS):
            self.ntT()
            self.ntListaE()
            return
        else:

            errorList.append(
            "ErrorType: simbolo no permitido, se esperaba un '(', una letra o numero al inicio de la expresion o hay un par de parentesis vacio ")


    def ntListaE(self):
        
        if(self.curr_char == '|'):
            self.Next()
            self.ntT()
            self.ntListaE()
            return
        if (self.curr_char == ')' or self.curr_char == None or self.curr_char == '('):
            return
        else:

            errorList.append(
                "ErrorType: simbolo no  permitido, se esperaba un '|' o ')' ")


    def ntT(self):
        if (self.curr_char == '(' or self.curr_char in LETTERS):
            self.ntP()
            self.ntListaT()
            return
        else:

            errorList.append(
                "ErrorType:  simbolo no permitido, se esperaba  una letra o un numero ")


    def ntListaT(self):
        if(self.curr_char == '.'):
            self.Next()
            self.ntP()
            self.ntListaT()
            return
        if(self.curr_char == '|' or self.curr_char == ')' or self.curr_char == '(' ): #no funciona cuando hay un cierre parentesis nono aiuda
            return
        if(self.curr_char == None):
            return
        else:
            errorList.append(
                "ErrorType: simbolo no permitido, se esperaba un '|' o un '.' entre simbolos o expresiones o no cerro un paretesis ")


    def ntP(self):
        if (self.curr_char == '(' or self.curr_char in LETTERS):
            self.ntOpt()
            self.ntMod()
            return
        else:

            errorList.append(
                "ErrorType: simbolo  no  permitido, se esperaba un letra o numero' ")


    def ntOpt(self):
        if(self.curr_char == '('):
            self.Next()
            self.ntE()
            if (self.curr_char == ')'):
                self.Next()
                return
        if(self.curr_char in LETTERS):
            self.Next()
            return
        else:
            errorList.append(
                "ErrorType: simbolo no  permitido, se esperaba una letra o numero ")


    def ntMod(self):
        if(self.curr_char == '*'):
            self.Next()
            return
        if(self.curr_char == '+'):
            self.Next()
            return
        if(self.curr_char == '.' or self.curr_char == None ):
            return


    def listError (self):
        print("dsfsafd")
        return errorList
    

