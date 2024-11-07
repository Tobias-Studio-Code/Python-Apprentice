"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""
from tkinter import messagebox, simpledialog, Tk

number1 = simpledialog.askinteger("title","enter number")
number2 = simpledialog.askinteger("title","enter number")
type_input = simpledialog.askstring("title","enter string!")

def all_input(number1,number2,type_input):

    answer = 0

    number1 = int(number1)

    number2 = int(number2)


    if type_input == "-":
        answer = number1 - number2

    elif type_input == "/":
         answer = number1 / number2

    elif type_input == "+":
        answer = number1 + number2

    elif type_input == "x":
        answer = number1 * number2
    
    return answer

answer = all_input(number1,number2,type_input)

messagebox.showinfo("", answer)

