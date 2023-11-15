# Write your solution here

# Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

num_1 = int(input("Number 1: "))
num_2 = int(input("Number 2: "))
oper = input("Operation: ")

if oper == "add":
    sum = num_1 + num_2
    print(f"{num_1} + {num_2} = {sum}")
elif oper == "subtract":
    sum = num_1 - num_2
    print(f"{num_1} - {num_2} = {sum}")
elif oper == "multiply":
    product = num_1 * num_2
    print(f"{num_1} * {num_2} = {product}")