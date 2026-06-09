#Activity 2: Swap Cases
#Problem Statement: How to swap all uppercase characters to lowercase and vice versa?
# Questions: - How the user will enter the character?
#- How it will swap? - Which commands will be used to convert each other?

import keyword
print(keyword.kwlist)

x= int(5)
y=6
print(f"{x}")
print({y})
print(f"5 + 3 = {5 + 3}")
print(f"{x} + {y} = {x + y}")


userInput = input("Please enter a message")
print(f"{userInput}")

print(f"Swapping cases : {userInput.swapcase()}")
print(f"Title : {userInput.title()}")
