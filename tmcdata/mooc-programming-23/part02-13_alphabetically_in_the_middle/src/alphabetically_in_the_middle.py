# Write your solution here

#Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

#You may assume the letters will be either all uppercase, or all lowercase.

#Some examples of expected behaviour:

# 1st letter: 
# 2nd letter: c
# 3rd letter: p
# The letter in the middle is 

first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

if first > second and first < third or first < second and first > third:
    middle = first
elif second > first and second < third or second < first and second > third:
    middle = second
else:
    middle = third
print(f"The letter in the middle is {middle}")