# Write your solution here

# Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed:

# Sample output
# Limit: 2
# The consecutive sum: 1 + 2 = 3
# Sample output
# Limit: 10
# The consecutive sum: 1 + 2 + 3 + 4 = 10
# Sample output
# Limit: 18
# The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

limit = int(input("Limit: "))
start = 1
add = 1
addition = "1"

while start < limit:
    add += 1
    start += add
    if start == limit or start > limit:
        addition += " + " + str(add) + " = " 
    else:
        addition += " + " + str(add)
print("The consecutive sum: " + addition + f"{start}")