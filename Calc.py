num1 = int(input("Choose your first number"))
operation = (input("Choose an operation.(+,-,*,/,root,^)"))
num2 = int(input("Choose your second number"))
if operation == "*":
    x = 0
    for i in range(num2):
        x += num1
    print(x)
if operation == "+": 
    print(num1 + num2)
if operation == "-":
    print(num1 - num2)
if operation == "/":
    print(num1 / num2)
if operation == "^":
    print(num1 ** num2)
if operation == "root":
    print(num1 ** (1/num1))