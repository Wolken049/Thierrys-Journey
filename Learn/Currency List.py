from tkinter import *

top = Tk()

top.geometry("600x300")

listbox1 = Listbox(top, height = 3,
                  width = 25,
                  x = 10,
                  bg = "#aaaaaa",
                  fg = "#0000aa",
                  activestyle = 'dotbox')



label1 = Label(top, text = "FromCurr")

listbox1.insert(1, "US Dollar")
listbox1.insert(2, "EUR Euro")
listbox1.insert(3, "GBR Pound")
listbox1.insert(4, "CHR Frank")
listbox1.insert(5, "JPY YEN")
listbox1.insert(6, "CNY Yuan")
listbox1.insert(7, "SEK Swedish Krona")
listbox1.insert(8, "NOK Norwegian Krone")
listbox1.insert(9, "DKK, Danish Krone")
listbox1.insert(10, "RUB Ruble")
listbox1.insert(11, "BWP Pula")

label1.pack()
listbox1.pack()

listbox2 = Listbox(top, height = 3,
                  width = 25,
                  x = 50,
                  bg = "#aaaaaa",
                  fg = "#0000aa",
                  activestyle = 'dotbox')

label2 = Label(top, text = "Tocurr")

listbox2.insert(1, "US Dollar")
listbox2.insert(2, "EUR Euro")
listbox2.insert(3, "GBR Pound")
listbox2.insert(4, "CHR Frank")
listbox2.insert(5, "JPY YEN")
listbox2.insert(6, "CNY Yuan")
listbox2.insert(7, "SEK Swedish Krona")
listbox2.insert(8, "NOK Norwegian Krone")
listbox2.insert(9, "DKK, Danish Krone")
listbox2.insert(10, "RUB Ruble")
listbox2.insert(11, "BWP Pula")

label2.pack()
listbox2.pack()

top.mainloop()