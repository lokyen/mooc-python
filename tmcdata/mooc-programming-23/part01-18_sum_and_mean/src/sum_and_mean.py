# Write your solution here

# Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

number_one = int(input("Number 1: "))
number_two = int(input("Number 2: "))
number_three = int(input("Number 3: "))
number_four = int(input("Number 4: "))

sum = number_one + number_two + number_three + number_four
mean = sum / 4.0
print(f"The sum of the numbers is {sum} and the mean is {mean}")