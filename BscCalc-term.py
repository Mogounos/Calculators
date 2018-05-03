#Project: Basic Calculator-Term
#Developer(s): Mogounos
#Creation Date: 2018/04/19
#Description: Terminal calculator with basic functionality (addition, subtraction, division, multiplication)
#===========================================================================
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#===========================================================================
import sys
#---------------------------------------------------------------------------

def Quit() :
#===========================================================================
#'Quit' exits the program
#===========================================================================
    sys.exit(0)


def CalAdd(a, b) :
#===========================================================================
#CalAdd adds two numbers
#===========================================================================
    retVal = 0
    retVal = a + b

    return print(retVal)


def CalSubtr(a, b) :
#===========================================================================
#CalSubtr subtracts two numbers
#===========================================================================
    retVal = 0
    retVal = a - b

    return print(retVal)


def CalMult(a, b) :
#===========================================================================
#CalMult multiplies two numbers
#===========================================================================
    retVal = 0
    retVal = a * b

    return print(retVal)


def CalDiv(a, b) :
#===========================================================================
#CalDiv divides two numbers
#===========================================================================
    retVal = 0
    try :
        retVal = a / b
        return print(retVal)
        
    except ZeroDivisionError :
        print("Cannot divide by 0!")
        return

    
#===========================================================================
#Main (loops indefinitely) [things to add: concatenate large numbers]
#===========================================================================
if (__name__=='__main__') :
    print("Welcome to this fantastically simple calculator! Type 'exit' anytime to terminate the program.")
  
    while True :
        Num1 = ''
        Operator = ''
        Num2 = ''
        x = 0

        while (x == 0) :
            try :
                
                Num1 = input("Enter Number >")
                Num1 = int(Num1)
                x = 1
            except :
                if (Num1 == 'exit') :
                    Quit()
                else :
                    print("That's not a valid number!")

#Needs simplification/optimization
        while (Operator!='+' and Operator!='-' and Operator!='*' and
               Operator!='/') :
            Operator = input("Enter Operation (+,-,*,/)>")
            if (Operator == 'exit') :
                Quit() 
            elif (Operator!='+' and Operator!='-' and Operator!='*' and
                Operator!='/') :
                print("That's not a valid operation!")
            else :
                x = 0


        while (x == 0) :
            try :
                Num2 = input("Enter Number >")
                Num2 = int(Num2)
                x = 1
            except :
                if (Num2 == 'exit') :
                    Quit()
                else :
                    print("That's not a valid number!")


#Needs simplification/optimization        
        if (Operator == '+') :
            x = CalAdd(Num1, Num2)
        elif (Operator == '-') :
            x = CalSubtr(Num1, Num2)
        elif (Operator == '*') :
            x = CalMult(Num1, Num2)
        elif (Operator == '/') :
            x = CalDiv(Num1, Num2)

        

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
#2018/04/30|+++|Troubleshooted errors and exceptions, added clear function and
        #button, moved terminal code to separate program
#
