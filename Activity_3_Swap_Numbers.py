#Problem Statement:Swap the numbers with and without the 3rd Variable.

#Questions:- How you will create and store the value in 3rd variable?
#- How you will do it without the 3rd Variable?

#with 3rd variable
number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))
print(f"Before swapping number with 3rd variable : {number1}, {number2}")

temp = number2
number2 = number1
number1 = temp
print(f"After swapping number with 3rd variable : {number1}, {number2}")

#without 3rd variable
print(f"\n Number1: {number1} Number2: {number2}")
number2 = number1 + number2
number1 = number2 - number1
number2 = number2 - number1
print(f"After swapping number without 3rd variable : Number1: {number1}, Number2: {number2}")

number1, number2 = number2, number1
print(f"\n Tuple swap :number1, number2 = number2, number1 : Number1: {number1}, Number2: {number2}")