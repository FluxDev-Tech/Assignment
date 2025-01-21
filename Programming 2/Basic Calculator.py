#ito yung mga pagpipilian natin kung ano ang gusto natin i-calculate
print("1. Addition: ")
print("2. Subtraction: ")
print("3. Multiplication: ")
print("4. Division: ")
chooseoption = int(input("Choose An Option Provided Above: "))
result = 0  # ito yung viriable natin na nagtatago ng calculate natin, Dito, gumagawa tayo ng isang variable na tinatawag na result at binibigyan ito ng initial value na 0

# print the first and second number
if chooseoption in (1, 2, 3, 4):
    number1 = float(input("Enter The First Number: "))
    number2 = float(input("Enter The Second Number: "))

    if chooseoption == 1:  #ang if,elif,else yan yung tinatawag na control flow statement na gumagawa ng conditional execution
        result = number1 + number2
    elif chooseoption == 2:
        result = number1 - number2
    elif chooseoption == 3:
        result = number1 * number2
    elif chooseoption == 4:
        if number2 != 0:
            result = number1 / number2
        else:
            print("Error: Division by zero is not allowed.")  # dito kung nag text ka nang false na number lalabas dyn ang error division
            result = None
    else:
        print("Invalid Option Chosen")  # if wala sa statement ang numbers mo

    # if calculate is true
    if result is not None:
        print("The Result of the Operation is:", result)

