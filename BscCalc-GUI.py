#Project: Basic Calculator-GUI
#Developer(s): Mogounos
#Creation Date: 2018/04/19
#Description: GUI calculator with basic functionality (addition, subtraction, division, multiplication)
#===========================================================================
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#===========================================================================
import tkinter as tk
from tkinter import messagebox
import sys
#---------------------------------------------------------------------------

varNum1 = ''
varOp = ''
varNum2 = ''
varFull = '0'
window = tk.Tk()
window.title("Calculator")
lbl = tk.Label(window, text = '')
lbl.grid(columnspan=3, row=0)


def Quit() :
#===========================================================================
#'quit' exits the program
#===========================================================================
    window.destroy()
    sys.exit(0)


def Clear() :
#===========================================================================
#'clear' resets the values so the calc can loop
#===========================================================================
    global varNum1
    global varOp
    global varNum2
    global varFull
    

    varNum1 = ''
    varOp = ''
    varNum2 = ''
    varFull = '0'

    lbl.configure(text = '')
    return


def CalAdd(a, b) :
#===========================================================================
#CalAdd adds two numbers
#===========================================================================
    retVal = 0
    retVal = a + b

    return retVal


def CalSubtr(a, b) :
#===========================================================================
#CalSubtr subtracts two numbers
#===========================================================================
    retVal = 0
    retVal = a - b

    return retVal


def CalMult(a, b) :
#===========================================================================
#CalMult multiplies two numbers
#===========================================================================
    retVal = 0
    retVal = a * b

    return retVal


def CalDiv(a, b) :
#===========================================================================
#CalDiv divides two numbers
#===========================================================================
    retVal = 0
    try :
        retVal = a / b
        return retVal
        
    except ZeroDivisionError :
        messagebox.showinfo("Error", "Cannot divide by 0!")
        return


def Clicked(a) :
#===========================================================================
#Inserts numbers and operators into variables on button press
#===========================================================================
    global varNum1
    global varOp
    global varNum2
    global varFull

    
    try :
        int(a)
        if (varFull.isnumeric() == True) :
            varNum1 = varNum1 + a
        else :
            varNum2 = varNum2 + a
    except :
        varOp = a

    varFull = varNum1 + varOp + varNum2
    lbl.configure(text = varFull)
    return


def Equals() :
#===========================================================================
#equals provides functionality to 'equal' button
#===========================================================================
    global varNum1
    global varOp
    global varNum2
    global varFull

    
    try :
        varNum1 = int(varNum1)
    except :
        messagebox.showinfo("Error", "Please enter two valid numbers and an operand!")
        Clear()
        return

    if (varOp == '') :
        messagebox.showinfo("Error", "Please enter a valid operand!")
        Clear()
        return
    
    try :
        varNum2 = int(varNum2)
    except :
        messagebox.showinfo("Error", "Please enter a valid number!")
        Clear()
        return
    
    if (varOp == '+') :
        x = CalAdd(varNum1, varNum2)
    elif (varOp == '-') :
        x = CalSubtr(varNum1, varNum2)
    elif (varOp == '*') :
        x = CalMult(varNum1, varNum2)
    elif (varOp == '/') :
        x = CalDiv(varNum1, varNum2)

    varFull = x
    lbl.configure(text = varFull)
    varNum1 = ''
    varOp = ''
    varNum2 = ''
    varFull = '0'
    return

    
#===========================================================================
#Main (loops indefinitely) [things to add: concatenate large numbers]
#===========================================================================
if (__name__=='__main__') :
  
    btn0 = tk.Button(window, text = "0", command = lambda : Clicked('0'), width = 4, height = 2)
    btn0.grid(column=0, row=1)
    btn1 = tk.Button(window, text = "1", command = lambda : Clicked('1'), width = 4, height = 2)
    btn1.grid(column=1, row=1)
    btn2 = tk.Button(window, text = "2", command = lambda : Clicked('2'), width = 4, height = 2)
    btn2.grid(column=2, row=1)
    btn3 = tk.Button(window, text = "3", command = lambda : Clicked('3'), width = 4, height = 2)
    btn3.grid(column=0, row=2)
    btn4 = tk.Button(window, text = "4", command = lambda : Clicked('4'), width = 4, height = 2)
    btn4.grid(column=1, row=2)
    btn5 = tk.Button(window, text = "5", command = lambda : Clicked('5'), width = 4, height = 2)
    btn5.grid(column=2, row=2)
    btn6 = tk.Button(window, text = "6", command = lambda : Clicked('6'), width = 4, height = 2)
    btn6.grid(column=0, row=3)
    btn7 = tk.Button(window, text = "7", command = lambda : Clicked('7'), width = 4, height = 2)
    btn7.grid(column=1, row=3)
    btn8 = tk.Button(window, text = "8", command = lambda : Clicked('8'), width = 4, height = 2)
    btn8.grid(column=2, row=3)
    btn9 = tk.Button(window, text = "9", command = lambda : Clicked('9'), width = 4, height = 2)
    btn9.grid(column=0, row=4)
    btnA = tk.Button(window, text = "+", command = lambda : Clicked('+'), width = 4, height = 2)
    btnA.grid(column=1, row=4)
    btnS = tk.Button(window, text = "-", command = lambda : Clicked('-'), width = 4, height = 2)
    btnS.grid(column=2, row=4)
    btnM = tk.Button(window, text = "*", command = lambda : Clicked('*'), width = 4, height = 2)
    btnM.grid(column=0, row=5)
    btnD = tk.Button(window, text = "/", command = lambda : Clicked('/'), width = 4, height = 2)
    btnD.grid(column=1, row=5)
    btnEq = tk.Button(window, text = "=", command = Equals, width = 4, height = 2)
    btnEq.grid(column=2, row=5)
    btnCl = tk.Button(window, text = "C", command = Clear, width = 4, height = 2)
    btnCl.grid(column=0, row=6)
    btnQ = tk.Button(window, text = "Quit", command = Quit, width = 9, height = 2)
    btnQ.grid(column=1, row=6, columnspan=2)
    window.mainloop()


#===========================================================================
#Version Control
#===========================================================================
#Format:Date Modified|+++|Notes
#===========================================================================
#2018/04/19|+++|Creation
#2018/04/23|+++|fixed broken Operator loop in main, added calculation methods
        #to main, attempted to add division by 0 exception
#2018/04/24|+++|fixed broken division by 0 exception, started work on GUI
#2018/04/25|+++|Optimized the process of changing Num1/Num2 to int()
#2018/04/26|+++|Attempted to rework number and operation check in main, worked
        #on GUI (buttons)
#2018/04/27|+++|Added functionality to display output to GUI,
#2018/04/30|+++|Troubleshot various errors and exceptions, added Clear function
        #and button, moved terminal code to separate program, added quit
        #function and button
#
