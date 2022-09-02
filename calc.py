operator = input("Please input an operator:\n")
num1 = float(input("Input first number:\n"))
num2 = float(input("Input second number:\n"))

if operator == "+":
    num3 = num1 + num2
    print(num3)

elif operator == "-":
    num3 = num1 - num2
    print(num3)

elif operator == "*":
    num3 = num1 * num2
    print(num3)
    
elif operator == "/":
    num3 = num1 / num2
    print(num3)

else:
    print("Invalid")