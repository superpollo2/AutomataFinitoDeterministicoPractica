FONT_NAME = FONT_NAME

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
regu_expresion = StringVar()
valid_string = StringVar()

# interfaz grafica


def create_gui():
    global valid_string_button
    global valid_string_entry
    window.resizable(0, 0)
    window.geometry('500x250+700+250')
    window.title("Practica l")
    window.config(bg='white')
    main_frame = tkinter.Frame(window)
    main_frame.pack()
    main_frame.config(width=480, height=320, bg='white')

    titl = tkinter.Label(
        main_frame, text="CONSTRUCIÓN DE AFD EN BASE A UN EXPRESIÓN REGULAR")
    titl.grid(column=0, row=0, padx=20, pady=20, columnspan=4)
    titl.config(bg='white', font=(FONT_NAME, 12))

    regu_expresion_label = tkinter.Label(main_frame, text="Expresión regular")
    regu_expresion_label.grid(column=0, row=1)
    regu_expresion_label.config(bg='white', font=(FONT_NAME, 12))
    valid_string_label = tkinter.Label(main_frame, text="String para comprobar")
    valid_string_label.grid(column=0, row=2, padx=10)
    valid_string_label.config(bg='white', font=(FONT_NAME, 12))

    # entradas de texto

    regu_expresion_entry = tkinter.Entry(main_frame, textvariable=regu_expresion)
    regu_expresion_entry.grid(column=1, row=1, columnspan=2)
    regu_expresion_entry.config(width=25)

    valid_string_entry = tkinter.Entry(main_frame, textvariable=valid_string,)
    valid_string_entry.grid(column=1, row=2, ipadx=2,
                          ipady=2, padx=5, pady=10, columnspan=2)
    valid_string_entry.config(state='disabled', width=25)

    # btn

    gen_afd_button = tkinter.Button(
        main_frame, text="Generar AFD", command=gen_afd)
    gen_afd_button.grid(column=3, row=1, ipadx=2, ipady=2, padx=10, pady=10)
    gen_afd_button.config(bg='#52CBD2', fg='#FFFDFD', font=(FONT_NAME, 12), relief='flat',
                        activebackground='#42A5AB', activeforeground='#FFFDFD', borderwidth=2)

    valid_string_button = tkinter.Button(
        main_frame, text="Validar", command=valid)
    valid_string_button.grid(column=3, row=2, ipadx=2, ipady=2, padx=10, pady=10)
    valid_string_button.config(bg='#52CBD2', fg='#FFFDFD', font=(FONT_NAME, 12), relief='flat',
                             activebackground='#42A5AB', activeforeground='#FFFDFD', borderwidth=2, state='disabled', width=10)

    clear_button = tkinter.Button(main_frame, text="Limpiar", command=clear)
    clear_button.grid(column=0, row=3, ipadx=2, ipady=2,
                     padx=10, pady=10, columnspan=4)
    clear_button.config(bg='#52CBD2', fg='#FFFDFD', font=(FONT_NAME, 12), relief='flat',
                       activebackground='#42A5AB', activeforeground='#FFFDFD', borderwidth=2, width=15)
    window.mainloop()


def gen_afd():

    global direct_tree
    global direct_reader

    if regu_expresion.get() == '':
        messagebox.showinfo("Advertencia", "Campo vacio\npor favor corrijalo")
    if regu_expresion.get() != '':
        valid = ValidExpresion(regu_expresion.get())
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
                reader = Reader(regu_expresion.get())
                tokens = reader.create_tokens()
                parser = Parser(tokens)
                direct_tree = direct_parser.Parse()
                messagebox.showinfo("Aceptada", tree)
                valid_string_button.config(state='normal')
                valid_string_entry.config(state='normal')
               

            except Exception as e:
                messagebox.showinfo("ERRPR: ", e)
            


def valid():
    if regu_expresion.get() == '':
        messagebox.showinfo("Advertencia", "Campo vacio")
    else:
        ddfa = DDFA(direct_tree, direct_reader.get_symbols(), valid_string.get())
        ddfa_regex = ddfa.EvalRegex()
        messagebox.showinfo(
            "Pertenece la cadena a la expresión regular?", ddfa_regex)
        valid_string.set("")
        

def clear():
    regu_expresion.set("")
    valid_string.set("")
    valid_string_button.config(state='disabled')
    valid_string_entry.config(state='disabled')

    


if __name__ == "__main__":
    create_gui()
