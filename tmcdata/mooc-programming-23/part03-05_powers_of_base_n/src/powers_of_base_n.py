# Write your solution here

# Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).

# Sample output
# Upper limit: 27
# Base: 3
# 1
# 3
# 9
# 27

limit = int(input("Upper limit: "))
base = int(input("Base: "))

start = 1

while start <= limit:
    print(start)
    start *= base