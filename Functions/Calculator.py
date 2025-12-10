from tkinter import *
import tkinter as tk
from Calcfunc.Addition import addition
from Calcfunc.Subtraction import subtraction
from Calcfunc.Multiplication import multiplication
from Calcfunc.Division import division
from Calcfunc.Percentage import percent



def basic_calculator():
    application = Tk()
    application.geometry("400x700")
    application.title("Base_Calculator")
    application.config(bg="#000000")

    button_frame = Frame(application, bg="#000000")
    button_frame.pack(fill = 'both', expand =True, padx=10, pady=10,)

    entry_font = ("Segoe UI", 50)
    entry_a = Entry(application, font=entry_font, fg="#ccccdd", bg="#000044")
    entry_b = Entry(application, font=entry_font, fg="#ccccdd", bg="#000044")
    entry_symbol = Label(application, font=entry_font, fg="#ccccdd", bg="#000044")
    result_label = Label(application, font=entry_font, text="", fg="#aaaadd", bg="#000066")
    entry_a.place(x = 5, y = 10, width=163, height=75)
    entry_b.place(x = 272, y = 10, width=153, height=75)
    entry_symbol.place(x = 170, y = 10, width=100, height=75)
    result_label.place(x = 1, y = 100, width=420, height=75)

    input_target = 'a'
    current_operator = None

    def set_input_target(t):
        nonlocal input_target
        input_target = t
        entry_a.config(bg="#333366" if t != 'a' else "#555588")
        entry_b.config(bg="#333366" if t != 'b' else "#555588")

    def insert_digit(d):
        target = entry_a if input_target == 'a' else entry_b
        if d == '.':
            current = target.get()
            if '.' in current:
                return
            if current == '' or current == '-':
                target.insert(END, "0.")
            else:
                target.insert(END, '.')
            return         
        target.insert(END, str(d))
        
    def toggle_negative(e):
        target = entry_a if input_target == 'a' else entry_b
        if e == '-':
            current = target.get()
            if current.startswith('-'):
                target.delete(0,1)
            elif current != '':
                target.insert(0, '-')
            return
        target.insert(0, str(e))
        
    def Percent_operator(p):
        target = entry_a if input_target == 'a' else entry_b
        if p == '%':
            current = target.get()
            if current != '':
                res = percent(float(current)) #I GOT IT YAAAAAAAAAYAYYYYYYYYYYYYY
                target.delete(0, END)
                target.insert(0, res)
            return
        target.insert(text=str(res))
        
    def set_operator(op):
        nonlocal current_operator
        current_operator = op
        set_input_target('b')
        entry_symbol.config(text=op)
        
    def do_equal():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            if current_operator == '+':
                res = addition(a, b)
            elif current_operator == '-':
                res = subtraction(a, b)
            elif current_operator == '*':
                res = multiplication(a, b)
            elif current_operator == '/':
                res = division(a, b)
            else:
                result_label.config(text='no op')
                return
            result_label.config(text=str(round(res, 3)))
        except Exception:
            result_label.config(text='error')

    def empty():
        entry_a.delete(0, END)
        entry_b.delete(0, END)
        entry_symbol.config(text="")
        result_label.config(text="")
        set_input_target('a')

    entry_a.bind("<FocusIn>", lambda e: set_input_target('a'))
    entry_b.bind("<FocusIn>", lambda e: set_input_target('b'))

    button_font = ("Georgia")

    C = Button(button_frame, text='C', padx=60, pady=35, command=empty, fg="#00aa00", bg="#ffff00")
    Percent = Button(button_frame, text='%', padx=60, pady=35, command=lambda: Percent_operator('%'), fg="#00aa00", bg="#ffff00")#Ich bin ein Idiot oida, wie ich vergessen kann
    Value0 = Button(button_frame, text = 0, padx=35, pady=35, command=lambda: insert_digit(0), fg="#000000", bg="#00cccc")
    Value1 = Button(button_frame, text = 1, padx=35, pady=35, command=lambda: insert_digit(1), fg="#ffffff", bg="#880000")
    Value2 = Button(button_frame, text = 2, padx=35, pady=35, command=lambda: insert_digit(2), fg="#ffffff", bg="#cc8800")
    Value3 = Button(button_frame, text = 3, padx=35, pady=35, command=lambda: insert_digit(3), fg="#ffffff", bg="#cccc00")
    Value4 = Button(button_frame, text = 4, padx=35, pady=35, command=lambda: insert_digit(4), fg="#ffffff", bg="#cccc00")
    Value5 = Button(button_frame, text = 5, padx=35, pady=35, command=lambda: insert_digit(5), fg="#ffffff", bg="#880000")
    Value6 = Button(button_frame, text = 6, padx=35, pady=35, command=lambda: insert_digit(6), fg="#ffffff", bg="#cc8800")
    Value7 = Button(button_frame, text = 7, padx=35, pady=35, command=lambda: insert_digit(7), fg="#ffffff", bg="#cc8800")
    Value8 = Button(button_frame, text = 8, padx=35, pady=35, command=lambda: insert_digit(8), fg="#ffffff", bg="#cccc00")
    Value9 = Button(button_frame, text = 9, padx=35, pady=35, command=lambda: insert_digit(9), fg="#ffffff", bg="#880000")
    Addition = Button(button_frame, text="+", padx=35, pady=35, command=lambda: set_operator('+'), fg="#cccccc", bg="#00aa00")
    Subtraction = Button(button_frame, text="-", padx=35, pady=35, command=lambda: set_operator('-'), fg="#cccccc", bg="#00aa00")
    Multiplication = Button(button_frame, text="*", padx=35, pady=35, command=lambda: set_operator('*'), fg="#cccccc", bg="#00aa00")
    Division = Button(button_frame, text="/", padx=35, pady=35, command=lambda: set_operator('/'), fg="#cccccc", bg="#00aa00")
    Equal = Button(button_frame, text="=", padx=35, pady=35, command=do_equal, fg="#ffffff", bg="#006600")
    Decimal = Button(button_frame, text=".", padx=35, pady=35, command=lambda: insert_digit('.'), fg="#ffffff", bg="#0066aa")
    Negative = Button(button_frame, text="+/-", padx=33, pady=33, command=lambda: toggle_negative('-'), fg="#ffffff", bg="#0066aa")

    C.place(x = 1, y = 200)
    Percent.place(x = 145, y = 200)
    Value0.place(x = 100, y = 600)
    Value1.place(x = 1, y = 500)
    Value2.place(x = 100, y = 500)
    Value3.place(x = 200, y =500)
    Value4.place(x = 1, y = 400)
    Value5.place(x = 100, y = 400)
    Value6.place(x = 200, y = 400)
    Value7.place(x = 1, y = 300)
    Value8.place(x = 100, y = 300)
    Value9.place(x = 200, y = 300)
    Addition.place(x = 300, y = 500)
    Subtraction.place(x = 300, y = 400)
    Multiplication.place(x = 300, y = 300)
    Division.place(x = 300, y = 200)
    Equal.place(x = 300, y = 600)
    Decimal.place(x = 200, y = 600)
    Negative.place(x = 1, y = 600)
    application.mainloop()
    
def scientific_calculator():
    application = Tk()
    application.geometry("400x700")
    application.title("Base_Calculator")
    application.config(bg="black")

    button_frame = Frame(application, bg="#000033")
    button_frame.pack(fill = 'both', expand =True, padx=10, pady=10,)

    entry_font = ("Segoe UI", 50)
    entry_a = Entry(application, font=entry_font, fg="#ccccdd", bg="#333366")
    entry_b = Entry(application, font=entry_font, fg="#ccccdd", bg="#333366")
    entry_symbol = Label(application, font=entry_font, fg="#ccccdd", bg="#333366")
    result_label = Label(application, font=entry_font, text="", fg="#aaaadd", bg="#333399")
    entry_a.place(x = 5, y = 10, width=163, height=75)
    entry_b.place(x = 272, y = 10, width=153, height=75)
    entry_symbol.place(x = 170, y = 10, width=100, height=75)
    result_label.place(x = 15, y = 100, width=370, height=75)

    input_target = 'a'
    current_operator = None

    def set_input_target(t):
        nonlocal input_target
        input_target = t
        entry_a.config(bg="#333366" if t != 'a' else "#555588")# Ich habe eine "Song Cover" gesehen aber ich kann es nicht findet.
        entry_b.config(bg="#333366" if t != 'b' else "#555588")#Ich werde diese Video pausieren. Ach vergiss es

    def insert_digit(d):
        target = entry_a if input_target == 'a' else entry_b
        if d == '.':
            current = target.get()
            if '.' in current:
                return
            if current == '' or current == '-':
                target.insert(END, "0.")
            else:
                target.insert(END, '.')
            return         
        target.insert(END, str(d))
        
    def toggle_negative(e):
        target = entry_a if input_target == 'a' else entry_b
        if e == '-':
            current = target.get()
            if current.startswith('-'):
                target.delete(0,1)
            elif current != '':
                target.insert(0, '-')
            return
        target.insert(0, str(e))
        
    def Percent_operator(p):
        target = entry_a if input_target == 'a' else entry_b
        if p == '%':
            current = target.get()
            if current != '':
                res = percent(float(current)) #I GOT IT YAAAAAAAAAYAYYYYYYYYYYYYY
                target.delete(0, END)
                target.insert(0, res)
            return
        target.insert(text=str(res))
        
    def set_operator(op):
        nonlocal current_operator
        current_operator = op
        set_input_target('b')
        entry_symbol.config(text=op)
        
    def do_equal():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            if current_operator == '+':
                res = addition(a, b)
            elif current_operator == '-':
                res = subtraction(a, b)
            elif current_operator == '*':
                res = multiplication(a, b)
            elif current_operator == '/':
                res = division(a, b)
            else:
                result_label.config(text='no op')
                return
            result_label.config(text=str(round(res, 3)))
        except Exception:
            result_label.config(text='error')

    def empty():
        entry_a.delete(0, END)
        entry_b.delete(0, END)
        entry_symbol.config(text="")
        result_label.config(text="")
        set_input_target('a')

    entry_a.bind("<FocusIn>", lambda e: set_input_target('a'))
    entry_b.bind("<FocusIn>", lambda e: set_input_target('b'))

    button_font = ("Georgia")

    C = Button(button_frame, text='C', padx=60, pady=35, command=empty, fg="#ffffff", bg="#ffff00")
    Percent = Button(button_frame, text='%', padx=60, pady=35, command=lambda: Percent_operator('%'), fg="#ffffff", bg="#ffff00")#Ich bin ein Idiot oida, wie ich vergessen kann
    Value0 = Button(button_frame, text = 0, padx=35, pady=35, command=lambda: insert_digit(0), fg="#000000", bg="#00cccc")
    Value1 = Button(button_frame, text = 1, padx=35, pady=35, command=lambda: insert_digit(1), fg="#ffffff", bg="#880000")
    Value2 = Button(button_frame, text = 2, padx=35, pady=35, command=lambda: insert_digit(2), fg="#ffffff", bg="#cc8800")
    Value3 = Button(button_frame, text = 3, padx=35, pady=35, command=lambda: insert_digit(3), fg="#ffffff", bg="#cccc00")
    Value4 = Button(button_frame, text = 4, padx=35, pady=35, command=lambda: insert_digit(4), fg="#ffffff", bg="#cccc00")
    Value5 = Button(button_frame, text = 5, padx=35, pady=35, command=lambda: insert_digit(5), fg="#ffffff", bg="#880000")
    Value6 = Button(button_frame, text = 6, padx=35, pady=35, command=lambda: insert_digit(6), fg="#ffffff", bg="#cc8800")
    Value7 = Button(button_frame, text = 7, padx=35, pady=35, command=lambda: insert_digit(7), fg="#ffffff", bg="#cc8800")
    Value8 = Button(button_frame, text = 8, padx=35, pady=35, command=lambda: insert_digit(8), fg="#ffffff", bg="#cccc00")
    Value9 = Button(button_frame, text = 9, padx=35, pady=35, command=lambda: insert_digit(9), fg="#ffffff", bg="#880000")
    Addition = Button(button_frame, text="+", padx=35, pady=35, command=lambda: set_operator('+'), fg="#cccccc", bg="#00aa00")
    Subtraction = Button(button_frame, text="-", padx=35, pady=35, command=lambda: set_operator('-'), fg="#cccccc", bg="#00aa00")
    Multiplication = Button(button_frame, text="*", padx=35, pady=35, command=lambda: set_operator('*'), fg="#cccccc", bg="#00aa00")
    Division = Button(button_frame, text="/", padx=35, pady=35, command=lambda: set_operator('/'), fg="#cccccc", bg="#00aa00")
    Equal = Button(button_frame, text="=", padx=35, pady=35, command=do_equal, fg="#ffffff", bg="#006600")
    Decimal = Button(button_frame, text=".", padx=35, pady=35, command=lambda: insert_digit('.'), fg="#ffffff", bg="#0066aa")
    Negative = Button(button_frame, text="+/-", padx=33, pady=33, command=lambda: toggle_negative('-'), fg="#ffffff", bg="#0066aa")

    C.place(x = 300, y = 300)
    Percent.place(x = 145, y = 200)
    Value0.place(x = 100, y = 450)
    Value1.place(x = 100, y = 400)
    Value2.place(x = 150, y = 400)
    Value3.place(x = 200, y =400)
    Value4.place(x = 100, y = 350)
    Value5.place(x = 150, y = 350)
    Value6.place(x = 200, y = 350)
    Value7.place(x = 100, y = 300)
    Value8.place(x = 150, y = 300)
    Value9.place(x = 200, y = 300)
    Addition.place(x = 250, y = 402)
    Subtraction.place(x = 300, y = 400)
    Multiplication.place(x = 250, y = 350)
    Division.place(x = 300, y = 350)
    Equal.place(x = 300, y = 600)
    Decimal.place(x = 200, y = 455)
    Negative.place(x = 150, y = 455)
    application.mainloop()
    
Set_up = Tk()
Set_up.geometry("400x600")
Set_up.title("Calculators")
Set_up.config(bg="black")

buttom_frame = Frame(Set_up, bg="black")
buttom_frame.pack(fill = 'both', expand=True)

Basic = Button(buttom_frame, text="Basic Calculator", command=basic_calculator, padx=60, pady=20, fg = "#333366", bg = "#ccccff")
Scientific = Button(buttom_frame, text="Scientific Calculator", command=scientific_calculator, padx=60, pady=20, fg = "#333366", bg = "#ccccff")



Basic.place(x = 100, y = 100)
Scientific.place(x = 85, y = 200)

Set_up.mainloop()