#Write a code in python in which you can get “Fizz Buzz”
#  for all numbers which can be divided by (3, 5, 15). 
# The range should from (1 to 100).
print("Fizz Buzz Game")
count = 0

while(count < 100):
    count += 1
    ByThree = False
    ByFive = False
    if count%15 == 0:
         print(count, "FizzBuzz")
    if count%5 == 0:
        ByFive = True
  
    if ByThree == True and ByFive == True:
        print(count, "FizzBuzz")
    elif ByThree == True and ByFive == False:
          print(count, "Fizz")
    elif ByFive == True and ByThree == False:
        print(count,  "Buzz")
    else:
        print(count)
        

print("For Loop")
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)