"""
Problem Statement:
Create a game in which user guesses a random number in python.

Questions:
- How will generate random number and how will you set the range?
- How to add attempts in your code, that user can have only 5 attempts to play?
- How will you subtract a attempt when user plays it one time?
- How will you show the ‘YOU WON!’ and ‘YOU LOST’ message?
"""
import random

noOfAttempt = 5
# pythonNumber = 44 #User has to guess this number
pythonNumber = random.randint(0,50)
print("Rules for the \"Welcome to NUMBER GUESSING GAME!\" :")
print("User will have to guess the correct number and win the prize with only 5 attempts to guess it correctly\n")
while noOfAttempt > 0:
    try:
        userInput = int(input("Please enter a valid number in the range of (0-50) for the game: "))
        if(userInput == pythonNumber):
            print("Correct Guess!!")
            print("YOU WON!!")
            print(f"Random number generated was : {pythonNumber}")
            break;
        elif(userInput < pythonNumber and noOfAttempt !=1):
            noOfAttempt = noOfAttempt - 1
            print(f"You have {noOfAttempt} attempts remaining. ")
            print("Hint: The number is bigger than you entered.\n")
        elif(userInput > pythonNumber and noOfAttempt !=1):
             noOfAttempt = noOfAttempt - 1
             print(f"You have {noOfAttempt} attempts remaining. ")
             print("Hint: The number is smaller than you entered.\n")
        else:
            print("\nYou have exhausted all of your attempts. YOU LOST!! Better Luck next time!\n ")
            print(f"Random number generated was : {pythonNumber}")
            break
    except ValueError:
        noOfAttempt = noOfAttempt - 1
        print(f"You have {noOfAttempt} attempts remaining. ")
        #Checking for valid input
        print("Incorrect input value: Please enter a valid number!\n")

