from tkinter import *
import backend_code
from datetime import datetime as dt

ntime = dt.now().strftime("%Y-%m-%d %H:%M:%S")


def see_balance():
    with open("balance.txt", "r") as file:
        bal = file.read()
        bal = float(bal)
        l1.delete(0, END)
        l1.insert(END, bal)

def view_transactions():
    l1.delete(0, END)
    for row in backend_code.view():
        l1.insert(END, row)

def del_file():
    backend_code.delete()
    l1.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)


def insert_values():
    backend_code.add(amount.get(),ntime, msg.get())
    backend_code.add_balance(amount.get())

def deduct_values():
    backend_code.withdraw(amount.get(),ntime, msg.get())
    backend_code.deduct_balance(amount.get())

window = Tk()
window.wm_title("Personal finance")

m1 = Message(window, text = "Msg", width = 50)
m1.grid(column = 0, row = 1)
m2 = Message(window, text = "Amount", width = 50)
m2.grid(column = 0, row = 0)

amount = StringVar()
e1 = Entry(window, textvariable = amount)
e1.grid(column = 1, row =0)
msg = StringVar()
e2 = Entry(window, textvariable = msg)
e2.grid(column = 1, row =1)

b1 = Button(window, text = "Balance", width = 17, command = see_balance)
b1.grid(column =3, row = 3)
b2 = Button(window, text = "Add", width = 17, command =insert_values)
b2.grid(column = 3, row = 4)
b3 = Button(window, text = "Withdraw", width = 17, command =deduct_values)
b3.grid(column = 3, row = 5)
b4 = Button(window, text = "View Transactions", width = 17, command = view_transactions)
b4.grid(column = 3, row = 6)
b5 = Button(window, text = "Reset", width = 17, command = del_file)
b5.grid(column = 3, row = 7)
b6 = Button(window, text = "Close", width = 17, command = window.destroy)
b6.grid(column = 3, row = 8)

l1 = Listbox(window, height = 8 , width = 40)
l1.grid(column = 0 , row = 3, columnspan = 2 , rowspan = 7)
sb1 = Scrollbar(window)
sb1.grid(column = 2, row = 3, rowspan = 7)

#l1.bind('<<ListBoxSelect>>')

l1.configure(yscrollcommand = sb1.set)
sb1.configure(command = l1.yview)

window.mainloop()