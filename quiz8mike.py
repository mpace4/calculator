#quiz8, mike pace
from tkinter import *
import math
from tkinter import font as tkFont

root = Tk()
root.title("simple calculator")
fontsize = tkFont.Font(size=12)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#functions for button clickls
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global first_num
    global mathtype
    mathtype = "addition"
    first_num = int(first_number)
    e.delete(0, END)
    
def button_sub():
    first_number = e.get()
    global first_num
    global mathtype
    mathtype = "subtraction"
    first_num = int(first_number)
    e.delete(0, END)

def button_multi():
    first_number = e.get()
    global first_num
    global mathtype
    mathtype = "multiplication"
    first_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global first_num
    global mathtype
    mathtype = "division"
    first_num = int(first_number)
    e.delete(0, END)

def button_sqroot():
    first_number = e.get()
    global first_num
    global mathtype
    mathtype = "sqroot"
    first_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if mathtype == "addition":
        e.insert(0, first_num + int(second_number))

    if mathtype == "subtraction":
        e.insert(0, first_num - int(second_number))

    if mathtype == "multiplication":
        e.insert(0, first_num * int(second_number))
        
    if mathtype == "division":
        e.insert(0, first_num / int(second_number))

    if mathtype == "sqroot":
        newnum = math.sqrt(5)
        e.insert(0, math.sqrt(5))

def button_fontenlarge():
    global fontsize
    fontsize.configure(size = fontsize.cget('size') +1)


def button_fontsmall():
    fontsize.configure(size = fontsize.cget('size') -1)


#define buttons
button_1 = Button(root, font=fontsize, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, font=fontsize,text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, font=fontsize,text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, font=fontsize,text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, font=fontsize,text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, font=fontsize,text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, font=fontsize,text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, font=fontsize,text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, font=fontsize,text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, font=fontsize,text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, font=fontsize,text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, font=fontsize,text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, font=fontsize,text="clear", padx=79, pady=20, command=button_clear)

button_sub = Button(root, font=fontsize,text="-", padx=41, pady=20, command=button_sub)
button_multi = Button(root, font=fontsize,text="*", padx=39, pady=20, command=button_multi)
button_divide = Button(root, font=fontsize,text="/", padx=41, pady=20, command=button_divide)
button_sqroot = Button(root, font=fontsize,text="√ ", padx=39, pady=20, command=button_sqroot)

button_fontenlarge = Button(root, font=fontsize,text="big", padx=39, pady=20, command=button_fontenlarge)
button_fontsmall = Button(root, font=fontsize,text="small", padx=39, pady=20, command=button_fontsmall)
                      

#adds buttons to screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_multi.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

button_sqroot.grid(row=7, column=0)
button_fontenlarge.grid(row=7, column=1)
button_fontsmall.grid(row=7, column=2)
    
