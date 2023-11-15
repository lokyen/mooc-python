# Write your solution here

# Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.

name = input("Please tell me your name? ")

if name != "Jerry":
    num_portions = int(input("How many portions of soup? "))
    cost = num_portions * 5.90
    print(f"The total cost is {cost}")
print("Next please!")