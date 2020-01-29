from tkinter import *
import enum
import math

class Operation(enum.Enum):
    add = 1
    sub = 2
    mult = 3
    div = 4

num1 = None
num2 = None
operation = None
result_is_on_screen = False

def button_click(num):
    global result_is_on_screen
    if result_is_on_screen and num == '.':
        display.delete(0, END)
        display.insert(0, "0.")
        result_is_on_screen = False
        return
    elif result_is_on_screen:
        display.delete(0, END)
    current_input = display.get()
    if num == '0' and current_input == '0':
        return
    elif current_input == '0' and num != '.':
        display.delete(0, END)
        current_input = ''
    elif num == '.' and '.' in current_input:
        return
    if num == '.' and current_input == '':
        print('Hello')
        display.insert(0, "0.")
    current_input = current_input + num
    display.delete(0, END)
    display.insert(0, current_input)
    result_is_on_screen = False
def button_clear():
        display.delete(0, END)
        display.insert(0, '0')
def sign_change():
    num = get_number()
    num *= -1
    display.delete(0, END)
    display.insert(0, str(num))
def factorial(num):
    num = math.ceil(int(num))
    if num == 1:
        return 1
    return num * factorial(num-1)
def add():
    global num1, operation
    num1 = get_number()
    display.delete(0, END)
    operation = Operation.add
def subtract():
    global num1, operation
    num1 = get_number()
    display.delete(0, END)
    operation = Operation.sub
def multiply():
    global num1, operation
    num1 = get_number()
    display.delete(0, END)
    operation = Operation.mult
def divide():
    global num1, operation
    num1 = get_number()
    display.delete(0, END)
    operation = Operation.div
def equal_sign():
    global num1, num2, operation, result_is_on_screen
    num2 = get_number()
    if operation == Operation.add:
        display.delete(0, END)
        if num1 == 1488 and num2 == 228:
            display.delete(0, END)
            display.insert(0, "ЛЁХА, ТЫ ПИДОР")
            return
        display.insert(0, '{}'.format(set_number(num1 + num2)))
    elif operation == Operation.sub:
        display.delete(0, END)
        display.insert(0, '{}'.format(num1 - num2))
    elif operation == Operation.mult:
        display.delete(0, END)
        display.insert(0, '{}'.format(num1 * num2))
    elif operation == Operation.div:
        display.delete(0, END)
        display.insert(0, '{}'.format(set_number(num1 / num2)))
    num1 = num2 = None
    operation = None
    result_is_on_screen = True

def result_display(num):
    display.delete(0, END)
    display.insert(0, num)
def get_number():
    num = display.get()
    if type(num1) == type(float):
        num = float(num)

    if '.' in num:
        num = float(num)
    else:
        num = int(num)
    return num
def set_number(num):
    if ".0"  in str(num)[-2:]:
        num = int(num)
    elif '.' in str(num):
        num = float(num)
    else:
        num = int(num)
    return num




win = Tk()
screen_height = win.winfo_screenheight()

win.title("Calulator")
win.iconbitmap("/Users/vladsokolovskii/Desktop/python/gui_project/shit_icon.ico")
#win.geometry("330x500+0+{}".format(screen_height))
win.resizable(False, False)
win.wm_attributes("-alpha", 0.95)

display = Entry(win, width = 26, justify = "right")
display.grid(row = 0, column = 0, columnspan = 10, ipady = 6)
display.insert(0, '0')


#Definition of buttons
clear_button = Button(win, text = 'C', padx = 20, pady = 15, command = button_clear)
sign_button = Button(win, text = '+/-', padx = 20, pady = 15, command = sign_change)
fact_button = Button(win, text = 'x!', padx = 20, pady = 15, command = lambda: result_display(factorial(get_number())))
b1 = Button(win, text = '1', padx = 20, pady = 15, command = lambda: button_click('1'))
b2 = Button(win, text = '2', padx = 20, pady = 15, command = lambda: button_click('2'))
b3 = Button(win, text = '3', padx = 20, pady = 15, command = lambda: button_click('3'))
b4 = Button(win, text = '4', padx = 20, pady = 15, command = lambda: button_click('4'))
b5 = Button(win, text = '5', padx = 20, pady = 15, command = lambda: button_click('5'))
b6 = Button(win, text = '6', padx = 20, pady = 15, command = lambda: button_click('6'))
b7 = Button(win, text = '7', padx = 20, pady = 15, command = lambda: button_click('7'))
b8 = Button(win, text = '8', padx = 20, pady = 15, command = lambda: button_click('8'))
b9 = Button(win, text = '9', padx = 20, pady = 15, command = lambda: button_click('9'))
b0 = Button(win, text = '0', padx = 60, pady = 15, command = lambda: button_click('0'))
point_button = Button(win, text = ',', bg = 'blue', padx = 20, pady = 15, command = lambda: button_click('.'))
add_button = Button(win, text = '+', padx = 20, pady = 15, bg = "#FF6C00", command = add)
subtract_button = Button(win, text = '-', padx = 20, pady = 15, bg = "#FF6C00", command = subtract)
mult_button = Button(win, text = '×', padx = 20, pady = 15, bg = "#FF6C00", command = multiply)
div_button = Button(win, text = '÷', padx = 20, pady = 15, bg = "#FF6C00", command = divide)
equal_button = Button(win, text = '=', padx = 20, pady = 15, bg = "#FF6C00", command = equal_sign)


#Put the buttons on the screen
b1.grid(row = 4, column = 0, sticky="nsew")
b2.grid(row = 4, column = 1, sticky="nsew")
b3.grid(row = 4, column = 2, sticky="nsew")
b4.grid(row = 3, column = 0, sticky="nsew")
b5.grid(row = 3, column = 1, sticky="nsew")
b6.grid(row = 3, column = 2, sticky="nsew")
b7.grid(row = 2, column = 0, sticky="nsew")
b8.grid(row = 2, column = 1, sticky="nsew")
b9.grid(row = 2, column = 2, sticky="nsew")
b0.grid(row = 5, column = 0, columnspan = 2, sticky="nsew")
point_button.grid(row = 5, column = 2, sticky="nsew")
clear_button.grid(row = 1, column = 0, sticky="nsew")
sign_button.grid(row = 1, column = 1, sticky="nsew")
fact_button.grid(row = 1, column = 2, sticky="nsew")
div_button.grid(row = 1, column = 3, sticky="nsew")
mult_button.grid(row = 2, column = 3, sticky="nsew")
subtract_button.grid(row = 3, column = 3, sticky="nsew")
add_button.grid(row = 4, column = 3, sticky="nsew")
equal_button.grid(row = 5, column = 3, sticky="nsew")




win.mainloop()
