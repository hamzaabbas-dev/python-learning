# First Project - MINI CALCULATOR

choice = "yes"

while choice == "yes":

    a = float(input("Enter number a: "))
    b = float(input("Enter number b: "))

    op = input("Enter operator (+, -, *, /, **, %): ")

    if op == '+':
        print("Output =", a + b)

    elif op == '-':
        print("Output =", a - b)

    elif op == '*':
        print("Output =", a * b)

    elif op == '**':
        print("Output =", a ** b)

    elif op == '/':
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print("Output =", a / b)

    elif op == '%':
        if b == 0:
            print("Cannot find remainder when dividing by zero!")
        else:
            print("Output =", a % b)

    else:
        print("Invalid operation!")

    choice = input("\nDo you want to calculate again? (yes/no): ").lower()

print("\nThank you for using Mini Calculator!")