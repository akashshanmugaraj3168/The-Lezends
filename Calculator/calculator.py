from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, padx=50, pady=10, columnspan=5)


def button_click(number):
    global num
    exist = str(e.get())
    e.delete(0, END)
    e.insert(0, exist + str(number))
    num = exist + str(number)


def button_add():
    global f_num
    global operand
    first_num = e.get()
    operand = "addition"
    f_num = int(first_num)
    e.delete(0, END)


def button_equal():
    if operand == "addition":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num + int(second_num))
    elif operand == "subtraction":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num - int(second_num))
    elif operand == "multiplication":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num * int(second_num))
    elif operand == "division":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num / int(second_num))


def button_subtract():
    first_num = e.get()
    global f_num
    global operand
    operand = StringVar()
    operand = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)


def button_multiply():
    first_num = e.get()
    global f_num
    global operand
    operand = StringVar()
    operand = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)


def button_divide():
    first_num = e.get()
    global f_num
    global operand
    operand = StringVar()
    operand = "division"
    f_num = int(first_num)
    e.delete()


def clear():
    e.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=90, pady=20, command=lambda: button_click(0))
button_point = Button(root, text=".", padx=42, pady=20, command=button_click, state = DISABLED)
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_add)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_add)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_add)
print()
button_equal = Button(root, text="=", padx=90, pady=20, command=button_equal)
button_clear = Button(root, text="C", padx=90, pady=20, command=clear)

# arranging buttons
button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)

button_0.grid(row=4, column=0, columnspan=3)
button_point.grid(row=4, column=3)
button_add.grid(row=1, column=4)
button_subtract.grid(row=2, column=4)
button_multiply.grid(row=3, column=4)
button_divide.grid(row=4, column=4)
button_clear.grid(row=5, column=0, columnspan=3)
button_equal.grid(row=5, column=3, columnspan=3)

root.mainloop()
