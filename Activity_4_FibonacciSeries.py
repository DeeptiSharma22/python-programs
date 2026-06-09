#Problem Statement: Write a code in python which will give you a Fibonacci series to a number when you enter it.

#Questions:
#- How you will you deal when a user inputs ‘0’?
#- How the user will deal when a user inputs ‘1’?
#- Which loops and statements do you use for the iterations?

while True:
    try:
        number = int(input("Please enter the end term (F(n)) of Fibonacci series : "))
        counter=0
        i,j = 0,1
        FibonacciSeries = ()
        FibonacciSeries = FibonacciSeries + (i,)
        print(f"F{counter} : {FibonacciSeries}")
        #If condition added to check for user input '1'
        if(number >= 1):
            FibonacciSeries = FibonacciSeries + (j,)
            counter = counter +1
            print(f"F{counter} : {FibonacciSeries}")

        #For Loop used for iterations
        for counter in range(counter, number):
                counter =counter +1
                k = i + j
                i=j
                j=k
                FibonacciSeries = FibonacciSeries + (k,)
                #print(f"F({counter}  : {i}, {j}")
                print(f"F{counter} : {FibonacciSeries}")
        break
    except ValueError:
        print("Incorrect Input value: Please enter a valid number. \n")  


