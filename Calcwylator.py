#Calcwylator using Python 3 and tkinter

print("""Calcwylator Version 0.1.0  Copyright (C) 2016  Somewun
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.""")

from tkinter import *
from math import *
from tkinter.messagebox import *

#menu functions
def About():
    showinfo("Help", "This is a simple calculator using Python 3 and Tkinter. \nThis is going to be the help information.")

def license():
    showinfo("License",
             """Calcwylator, a simple lightweight calculator. Version 0.1.0.
                Copyright (C) 2016  Somewun

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.""")

#Maths functions
def evaluate():
    res.configure(text="Answer: " + str(eval(entry.get())))
    ans = float(eval(entry.get()))
    print(ans)

#Entry key functions
def zero():
    entry.insert(END, "0")
def one():
    entry.insert(END, "1")
def two():
    entry.insert(END, "2")
def three():
    entry.insert(END, "3")
def four():
    entry.insert(END, "4")
def five():
    entry.insert(END, "5")
def six():
    entry.insert(END, "6")
def seven():
    entry.insert(END, "7")
def eight():
    entry.insert(END, "8")
def nine():
    entry.insert(END, "9")
def point():
    entry.insert(END, ".")
def times():
    entry.insert(END, "*")
def divide():
    entry.insert(END, "/")
def plus():
    entry.insert(END, "+")
def minus():
    entry.insert(END, "-")
def openbrack():
    entry.insert(END, "(")
def closebrack():
    entry.insert(END, ")")

def clear():
    entry.delete(0, END)

w = Tk()
w.title("Calcwylator")
w.minsize(300,200)

menu = Menu(w)
w.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=w.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="About", menu=helpmenu)
helpmenu.add_command(label="Help", command=About)
helpmenu.add_command(label="License", command=license)

Label(w, text="Your Expression:").grid(row=0,column=0)
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.grid(row=0, column=1)
res = Label(w)
res.grid(row=0, column=2)

Button(text='7', command=seven).grid(row=1, column=0, ipadx=20)
Button(text='8', command=eight).grid(row=1, column=1, ipadx=20)
Button(text='9', command=nine).grid(row=1, column=2, ipadx=20)
Button(text='4', command=four).grid(row=2, column=0, ipadx=20)
Button(text='5', command=five).grid(row=2, column=1, ipadx=20)
Button(text='6', command=six).grid(row=2, column=2, ipadx=20)
Button(text='1', command=one).grid(row=3, column=0, ipadx=20)
Button(text='2', command=two).grid(row=3, column=1, ipadx=20)
Button(text='3', command=three).grid(row=3, column=2, ipadx=20)
Button(text='0', command=zero).grid(row=4, column=1, ipadx=20)

Button(text='.', command=point).grid(row=4, column=0, ipadx=21)
Button(text='=', command=evaluate).grid(row=4, column=2, ipadx=19)
Button(text='+', command=plus).grid(row=1, column=3, ipadx=18)
Button(text='-', command=minus).grid(row=2, column=3, ipadx=20)
Button(text='*', command=times).grid(row=3, column=3, ipadx=20)
Button(text='/', command=divide).grid(row=4, column=3, ipadx=20)
Button(text='(', command=openbrack).grid(row=1, column=4, ipadx=20)
Button(text=')', command=closebrack).grid(row=2, column=4, ipadx=20)
#Button(text='ans', command=ans).grid(row=3, column=4, ipadx=20)
Button(text='C', command=clear).grid(row=4, column=4, ipadx=20)

w.mainloop()
