# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

# In the Python math module there is the function sqrt, which calculates the square root of a number. You can use it like so:

# from math import sqrt

# print(sqrt(9))
# This should print out

# Sample output
# 3.0
# We will return to the concept of a module and the import statement later. For now, it is sufficient to understand that the line from math import sqrt allows us to use the sqrt function in our program.

# Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:

# x = (-b ± sqrt(b²-4ac))/(2a).

# You can assume the equation will always have two real roots, so the above formula will always work.

# An example of expected behaviour:

# Sample output
# Value of a: 1
# Value of b: 2
# Value of c: -8

# The roots are 2.0 and -4.0

value_a = int(input("Value of a: "))
value_b = int(input("Value of b: "))
value_c = int(input("Value of c: "))

square_root = float(sqrt((value_b ** 2) - (4 * value_a * value_c)))
root_1 = ((-(value_b) + square_root) / (2 * value_a))
root_2 = ((-(value_b) - square_root) / (2 * value_a))

print(f"The roots are {root_1} and {root_2}")