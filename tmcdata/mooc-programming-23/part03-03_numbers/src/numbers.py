# Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.

# Sample output
# Upper limit: 5
# 1
# 2
# 3
# 4


upper_limit = int(input("Upper limit: "))

num = 1
while num < upper_limit:
    print(num)
    num += 1