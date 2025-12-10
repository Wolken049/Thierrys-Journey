from tkinter import *

top = Tk()

listbox1 = Listbox(top, height = 3,
                  width = 15,
                  bg = "#ffffff",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "#ffff00")

listbox1.pack(pady = 20)

listbox2 = Listbox(top, height = 3,
                  width = 15,
                  bg = "#ffffff",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "#ffff00")

listbox2.pack(pady = 20)

Button_frame = Frame(top, bg = "#ffffff")
Button_frame.pack(fill = 'both', expand = True)

top.geometry("300x600")

label = Label(top, text = " FOOD ITEMS")

label.pack(pady = 10)

listbox1.insert(1, "Nachos")
listbox1.insert(2, "Sandwich")
listbox1.insert(3, "Burger")
listbox1.insert(4, "Pizza")
listbox1.insert(5, "Burrito")

listbox2.insert(1, "Nachos")
listbox2.insert(2, "Sandwich")
listbox2.insert(3, "Burger")
listbox2.insert(4, "Pizza")
listbox2.insert(5, "Burrito")

Conv = Button(Button_frame, text="Test2", width = 10, height = 5)

Conv.place(x = 100, y = 200)


top.mainloop()