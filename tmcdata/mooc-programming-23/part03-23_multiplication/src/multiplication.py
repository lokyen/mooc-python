# Write your solution here

# Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details:

# Sample output
# Please type in a number: 2
# 1 x 1 = 1
# 1 x 2 = 2
# 2 x 1 = 2
# 2 x 2 = 4

number = int(input("Please type in a number: "))

i = 1
while i <= number:
    j = 1
    while j <= number:
        print(f"{i} x {j} = {i * j}")
        j+= 1
    i+= 1