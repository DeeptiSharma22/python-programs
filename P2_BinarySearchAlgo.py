'''
Project 2: Problem Statement: You want to implement a Binary Search algorithm in Python to efficiently search for a target value in a sorted list.

Question: How can I write a Python program that uses the Binary Search algorithm to find a target value in a sorted list?
'''
#Sorted List of numbers
#sorted_list = [1,5,8,9,10,25,30,38,40]

def func_binary_search_algo(sortedList, userInput, start_index, last_index):
    print(f"\n Sorted List: {sortedList} \n")
    print(f"Value to be searched: {userInput} from position:{start_index} : {last_index} of list")
    if userInput not in [item for item in sortedList]:
        print(f"Invalid input {userInput} {sortedList}")
        return -1
    else:
        #Searching value in list
        search_from = start_index
        search_till = (start_index + last_index)//2 #finding mid-point
        print(f"search_from : {search_from} Search_till: {search_till} \n")
        if(sortedList[search_till] == userInput):
            print(f"Value found at position:{search_till} : sortedList[{search_till}] :{sortedList[search_till]}")
            return search_till
        elif(sortedList[search_till] < userInput):
            search_from = search_till + 1
            print(f"Searching now in [{search_from}]:[{last_index}]")
            return func_binary_search_algo(sortedList, userInput, search_from, last_index)
        elif(sortedList[search_till] > userInput):
            search_till = search_till - 1
            print(f"Searching now in [{start_index}]:[{search_till}]")
            return func_binary_search_algo(sortedList, userInput, start_index, search_till)
        else:
             print("Not found")
    

print("\n Binary Search Algorithm:")
sorted_list = [1,5,8,9,10,25,30,38,40]
print(f"Sorted List: {sorted_list}")
search_value = int(input("Enter the target value to be searched from the above list: "))
index = func_binary_search_algo(sorted_list, search_value,0,len(sorted_list)-1)
if(index != -1):
    print(f"Value found at index in list : {index}")