"""
Problem Statement: Create a Basic Calculator that can do Addition, Subtraction, Multiplication and Division in Python.

 Questions:
- How to create Choices for the user?
- How the user input two numbers?
- How can you add your define functions inside your If-else statements?
- How do stop the calculations at a certain part?
- How do you cope with this when a user will type a invalid input? */

"""


print("Hello! Basic Calculator")
while True:
        try:
                num1 = float(input("\n Enter the first number: "))
                operator = input("Enter an operator (+, -, *, /): ")
                num2 = float(input("Enter the second number: "))

                # Perform calculation using Dictionary amd lambda function

                result = {
                    '+': lambda a, b : a + b,
                    '-': lambda a, b : a - b,
                    '*': lambda a, b : a * b,
                    '/': lambda a, b : a / b if b != 0 else "Error! Division by zero.",
                }.get(operator, lambda a, b:"Invalid operator")(num1, num2)

                print("Result:", result)
                #break
        except:
                print("Inavlid input ERROR: Please enter a valid input.\n")


        # Perform calculation using if/else
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operator!"
            
        print("Result:", result)
        # Ask if the user wants to continue
        strContinue = input("\n Do you want to perform another calculation? (Y/N): ").strip().lower()
        if strContinue not in ('Y', 'y'):
            print("Thanks !")
            break