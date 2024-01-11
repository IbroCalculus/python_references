
def runCalculator():
    print("Enter an operation to carry out")
    print(" 1. ADDITION\n 2. SUBTRACTION\n 3. MULTIPLICATION\n 4. DIVISION")
    operation = int(input(">>> "))

    if operation == 1:
        print("You selected addition")
        fNumb = int(input("Enter first number: "))
        sNumb = int(input("Enter second number: "))

        answer = fNumb + sNumb
        print(f'{fNumb} + {sNumb} =  {answer}')

    elif operation == 2:
        print("You selected Subtraction")
        fNumb = int(input("Enter first number: "))
        sNumb = int(input("Enter second number: "))

        answer = fNumb - sNumb
        print(f'{fNumb} - {sNumb} =  {answer}')

    elif operation == 3:
        print("You selected Multiplication")
        fNumb = int(input("Enter first number: "))
        sNumb = int(input("Enter second number: "))

        answer = fNumb * sNumb
        print(f'{fNumb} * {sNumb} =  {answer}')

    elif operation == 4:
        print("You selected Division")
        fNumb = int(input("Enter first number: "))
        sNumb = int(input("Enter second number: "))

        if sNumb == 0:
            print("Division by zero is not allowed")
        else:
            answer = fNumb / sNumb
            print(f'{fNumb} / {sNumb} =  {answer}')


rerurnCalc = 1
while rerurnCalc == 1:
    runCalculator()
    x = input("Run calcular again?: y/n ")
    if x == "y":
        rerurnCalc = 1
    elif x== "n":
        rerurnCalc = 0

print("Program ended!")

