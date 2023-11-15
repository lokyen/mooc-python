# Write your solution here

# Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. The program should function as follows:

# Sample output
# Limit: 2
# 3
# Sample output
# Limit: 10
# 10
# Sample output
# Limit: 18
# 21

limit = int(input("Limit: "))
start = 1
add = 1

while start < limit:
    add += 1
    start += add
print(start)