"""
Project 1
Problem Statement:
You want to create a simple game of Rock-Paper-Scissors in Python that takes the input as Rock, Paper, or Scissors and allows you to compete against the computer.

Question:
How can you create a Python program that allows the player to play Rock-Paper-Scissors against the computer?
"""
import random


#Function: simple game of Rock-Paper-Scissors
def play_game():
    print("Rock-Paper-Scissors GAME \n")
    choices = ["r", "p", "s"] #rock(r) paper(p) scissors(s)

    while(True):
        userInput = input("Select your choice : Rock (R) Paper (P) Scissors (S) Exit (E)").lower()
        computerSelection = random.choice(choices)

        #Checking for valid user input
        if(userInput not in choices):
            print(f"You chose: {userInput}")
            print("Invalid input!")
            if input("Play again? (y/n): ").lower() != "y":
                break
            else:
                print("--------------------------------------")
                continue
        
        print(f"You chose: {userInput}")
        print(f"Computer chose: {computerSelection}")

        #Comparing the choices to decide the winner
        if(userInput == computerSelection):
            print("Its equal! A TIE \n")
            print("--------------------------------------")
        elif(userInput == "e"):
            print("Exit")
            break
        elif(
            (userInput == "p" and computerSelection == "r") or
            (userInput == "r" and computerSelection == "s") or
            (userInput == "s" and computerSelection == "p")
            ):
            print("User Won! \n")
            print("--------------------------------------")
        else:
            print("Computer Won! \n ")
            print("--------------------------------------")

#Calling the function
play_game()

