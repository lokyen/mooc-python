# Write your solution here

# Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.

# Sample output
# Please type in a string: test
# t
# st
# est
# test

word = input("Please type in a string: ")

count = len(word)
    
while count >= 0:

    print(word[(count):(len(word))])
    count -= 1