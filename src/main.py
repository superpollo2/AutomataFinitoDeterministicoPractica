
from reader_valid import ValidExpresion
from reader import Reader
from parsing import Parser
from afd import DDFA
from tkinter import  messagebox, ttk as ttk
import tkinter
from tkinter import StringVar, font
from turtle import title

# var global
window = tkinter.Tk()
reguExpresion = StringVar()
validString = StringVar()

# interfaz grafica


def createGUI():
    global validStringButton
    global validStringEntry
    window.resizable(0, 0)
    window.geometry('500x250+700+250')
    window.title("Practica l")
    window.config(bg='white')
    mainFrame = tkinter.Frame(window)
    mainFrame.pack()
    mainFrame.config(width=480, height=320, bg='white')

    titl = tkinter.Label(
        mainFrame, text="CONSTRUCIÓN DE AFD EN BASE A UN EXPRESIÓN REGULAR")
    titl.grid(column=0, row=0, padx=20, pady=20, columnspan=4)
    titl.config(bg='white', font=('Inria Sans Bold', 12))

    reguExpresionLabel = tkinter.Label(mainFrame, text="Expresión regular")
    reguExpresionLabel.grid(column=0, row=1)
    reguExpresionLabel.config(bg='white', font=('Inria Sans Regular', 12))
    validStringLabel = tkinter.Label(mainFrame, text="String para comprobar")
    validStringLabel.grid(column=0, row=2, padx=10)
    validStringLabel.config(bg='white', font=('Inria Sans Regular', 12))

    # entradas de texto

    reguExpresionEntry = tkinter.Entry(mainFrame, textvariable=reguExpresion)
    reguExpresionEntry.grid(column=1, row=1, columnspan=2)
    reguExpresionEntry.config(width=25)

    validStringEntry = tkinter.Entry(mainFrame, textvariable=validString,)
    validStringEntry.grid(column=1, row=2, ipadx=2,
                          ipady=2, padx=5, pady=10, columnspan=2)
    validStringEntry.config(state='disabled', width=25)

    # btn

    genAFDButton = tkinter.Button(
        mainFrame, text="Generar AFD", command=genAFD)
    genAFDButton.grid(column=3, row=1, ipadx=2, ipady=2, padx=10, pady=10)
    genAFDButton.config(bg='#52CBD2', fg='#FFFDFD', font=('Inria Sans Bold', 12), relief='flat',
                        activebackground='#42A5AB', activeforeground='#FFFDFD', borderwidth=2)

    validStringButton = tkinter.Button(
        mainFrame, text="Validar", command=valid)
    validStringButton.grid(column=3, row=2, ipadx=2, ipady=2, padx=10, pady=10)
    validStringButton.config(bg='#52CBD2', fg='#FFFDFD', font=('Inria Sans Bold', 12), relief='flat',
                             activebackground='#42A5AB', activeforeground='#FFFDFD', borderwidth=2, state='disabled', width=10)

    clearButton = tkinter.Button(mainFrame, text="Limpiar", command=clear)
    clearButton.grid(column=0, row=3, ipadx=2, ipady=2,
                     padx=10, pady=10, columnspan=4)
    clearButton.config(bg='#52CBD2', fg='#FFFDFD', font=('Inria Sans Bold', 12), relief='flat',
                       activebackground='#42A5AB', activeforeground='#FFFDFD', borderwidth=2, width=15)
    window.mainloop()


def genAFD():

    global direct_tree
    global direct_reader

    if reguExpresion.get() == '':
        messagebox.showinfo("Advertencia", "Campo vacio\npor favor corrijalo")
    if reguExpresion.get() != '':
        valid = ValidExpresion(reguExpresion.get())
        valid.ntE()
        
        errors = valid.listError()
        if len(errors):
            print("La expresión es inválida. Errores encontrados:")
            for error in errors:
                print(error)
                messagebox.showinfo("ErrorType: simbolo  no  permitido",error)
            
        else:
            try:
                print("La expresión es válida.")
                reader = Reader(reguExpresion.get())
                tokens = reader.create_tokens()
                parser = Parser(tokens)
                tree = parser.parse()
               

            except Exception as e:
                messagebox.showinfo("ERRPR: ", e)
            


def valid():
    if reguExpresion.get() == '':
        messagebox.showinfo("Advertencia", "Campo vacio")
    else:
        ddfa = DDFA(direct_tree, direct_reader.get_symbols(), validString.get())
        ddfa_regex = ddfa.EvalRegex()
        messagebox.showinfo(
            "Pertenece la cadena a la expresión regular?", ddfa_regex)
        validString.set("")
        pass


def clear():
    reguExpresion.set("")
    validString.set("")
    validStringButton.config(state='disabled')
    validStringEntry.config(state='disabled')

    pass


if __name__ == "__main__":
    createGUI()
