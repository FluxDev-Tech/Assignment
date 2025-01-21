def add(number1, number2):
    addition = number1 +number2
    print(addition)

def sub(number1, number2):
    subtraction = number1 - number2
    print(subtraction)

def multi(number1, number2):
    multi = number1 * number2
    print(multi)

def div(number1, number2):
    div = number1 / number2
    print(div)
 
sel = print("Select an operation: \n 1. + \n 2. - \n 3. * \n 4. / \n") #select operation
operation = int(input("Choose the number above = ")) 
number1 = int(input("Enter the first number: ")) #input first number
number2 = int(input("enter the second number: ")) #put second number
 
#start calculation
def calculate(number1, number2):
    if operation == 1:
        add(number1, number2)
    elif operation == 2:
        sub(number1, number2)
    elif operation == 3:
        multi(number1, number2)
    elif operation == 4:
        if number2 == 0:
            print("error")
        else:
            div(number1, number2)
 
calculate(number1, number2)