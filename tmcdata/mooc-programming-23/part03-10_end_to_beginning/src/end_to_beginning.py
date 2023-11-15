# Write your solution here

# Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a string: hiya
# a
# y
# i
# h

word = input("Please type in a string: ")
count = len(word)

while count > 0:
    print(word[count - 1])  
    count -= 1