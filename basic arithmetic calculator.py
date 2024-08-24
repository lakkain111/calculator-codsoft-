import math

def taking_input_from_user():
    a = float(input("Enter the first input number: "))
    b = float(input ("Enter the second input number: "))
    return a,b


def add (a,b):
    operation_add=a+b
    print("Addition: ",operation_add)
    return operation_add

def subtract(a,b):
    operation_subtract=a-b
    print("Subtraction: ",a-b)
    return operation_subtract

def division(a,b):
    while b == 0:
        print("WARNING: Invalid Equation! Try again!")
        b = float(input("Enter another number: "))
    operation_division = a / b
    print("Division: ",a/b)
    return operation_division

def multiplication(a,b):
    operation_multiplication=a*b
    print("Multiplication: ", a*b)
    return operation_multiplication

def history(calculations):
    print(calculations)

previous_calculations = []


while True:
    print("----------MENU----------")
    print("""Type an option:\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division """)
    click = float(input("Type an option: "))
    num_1, num_2=0,0

    if click >=1 and click <=4:
        num_1, num_2 = taking_input_from_user()

    if click == 1:
        operation=add(num_1,num_2)
        previous_calculations.append(operation)

    elif click ==2:
        operation = subtract(num_1, num_2)
        previous_calculations.append(operation)

    elif click == 3:
        operation = multiplication(num_1, num_2)
        previous_calculations.append(operation)

    elif click ==4:
        operation = division(num_1, num_2)
        previous_calculations.append(operation)

        break
    else:
        print("Invalid option")


