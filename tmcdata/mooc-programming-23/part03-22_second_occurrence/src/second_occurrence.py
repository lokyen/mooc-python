# Write your solution here

# Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

# In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

word = input("Please type in a string: ")
substr = input("Please type in a substring: ")

index = word.find(substr)
index_2 = -1

if index != -1:
    index_2 = word.find(substr, index + len(substr))
if index_2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {index_2}.")
    
    

    
