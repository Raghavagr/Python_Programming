from tkinter import *
from math import factorial
import parser

#make a top level tkinter window for our calculator
root = Tk()

# set the background color of your gui
root.configure(background="light blue")
root.geometry('300x180')
root.title('Crazy_Tech Calculator')

blankLine = Label(root, text="")
blankLine.grid()

#adding a input field(calculator screen)
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=N+E+W+S)

# declare var which will keep track of current pos on the input text field
i = 0

#recieve digit as parameter and display on input field
def get_variable(num):
    global i
    display.insert(i,num)
    i += 1

#mapping operator buttons
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i += length

#map AC button(clear screen)
def clear_all():
    display.delete(0,END)

#map undo function
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0,"Error")

def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

#step-2) designing a buttons

#code to add button to calculator
#row-2 after screen
Button(root, text="1", activebackground="green",fg="black",bg="red", height=1, width=7, 
command=lambda : get_variable(1)).grid(row=2, column=0, sticky=N+E+W+S)
Button(root, text="2", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_variable(2)).grid(row=2, column=1, sticky=N+E+W+S)
Button(root, text="3", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_variable(3)).grid(row=2, column=2, sticky=N+E+W+S)

#row-3
Button(root, text="4", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_variable(4)).grid(row=3, column=0, sticky=N+E+W+S)
Button(root, text="5", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_variable(5)).grid(row=3, column=1, sticky=N+E+W+S)
Button(root, text="6", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_variable(6)).grid(row=3, column=2, sticky=N+E+W+S)

#row-4
Button(root, text="7", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_variable(7)).grid(row=4, column=0, sticky=N+E+W+S)
Button(root, text="8", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_variable(8)).grid(row=4, column=1, sticky=N+E+W+S)
Button(root, text="9", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_variable(9)).grid(row=4, column=2, sticky=N+E+W+S)

#adding another buttons, row 5
Button(root, text="AC", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : clear_all()).grid(row=5, column=0, sticky=N+E+W+S)
Button(root, text="0", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_variable(0)).grid(row=5, column=1, sticky=N+E+W+S)
Button(root, text=".", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_variable('.')).grid(row=5, column=2, sticky=N+E+W+S)

#adding operator buttons, column 3(new column)
Button(root, text="+", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_operation("+")).grid(row=2, column=3, sticky=N+E+W+S)
Button(root, text="-", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_operation("-")).grid(row=3, column=3, sticky=N+E+W+S)
Button(root, text="*", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_operation("*")).grid(row=4, column=3, sticky=N+E+W+S)
Button(root, text="/", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_operation("/")).grid(row=5, column=3, sticky=N+E+W+S)

#adding some new operations
Button(root, text="pi", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_operation("*3.14")).grid(row=2, column=4, sticky=N+E+W+S)
Button(root, text="%", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_operation("%")).grid(row=3, column=4, sticky=N+E+W+S)
Button(root, text="(", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_operation("(")).grid(row=4, column=4, sticky=N+E+W+S)
Button(root, text="exp", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_operation("**")).grid(row=5, column=4, sticky=N+E+W+S)

Button(root, text="<-", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : undo()).grid(row=2, column=5, sticky=N+E+W+S)
Button(root, text="!", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : fact()).grid(row=3, column=5, sticky=N+E+W+S)
Button(root, text=")", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_operation(")")).grid(row=4, column=5, sticky=N+E+W+S)
Button(root, text="^2", activebackground="green",fg="black",bg="red", height=1, width=7, command=lambda : get_operation("**2")).grid(row=5, column=5, sticky=N+E+W+S)

#final put the = button for result
Button(root, text="=", activebackground="green",fg="black",bg="red", height=2, width=7, command=lambda : calculate()).grid(columnspan=6, sticky=N+E+W+S)

#call the mainloop to run code
root.mainloop()
