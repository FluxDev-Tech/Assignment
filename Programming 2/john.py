print("1. Addition: ")
print("2. Subtraction: ")
print("3. Multiplication: ")
print("4. Division: ")
chooseoption = int(input("Enter the number above: "))
result = 0

if chooseoption in (1, 2, 3, 4):
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    if chooseoption == 1:
        result = number1 + number2
    elif chooseoption == 2:
        result = number1 - number2
    elif chooseoption == 3:
        result = number1 * number2
    elif chooseoption == 4:
        if number2 != 0:
            result = number1 / number2
        else:
            print("Error: Division by sero is not allowed. ")
            reslut = None
    else:
        print("Invalid choosen")

    if result is not None:
        print("The result of the choosen is:", result)