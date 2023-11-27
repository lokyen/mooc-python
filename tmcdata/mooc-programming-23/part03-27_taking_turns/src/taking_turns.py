# Write your solution here

# Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

# Sample output
# Please type in a number: 5
# 1
# 5
# 2
# 4
# 3

number = int(input("Please type in a number: "))

num_printed_nums = 0
start = 1
end = number

while num_printed_nums < number:
    if start == end:
        print(start)
        break
    else:
        print(start)
        print(end)
        start += 1
        end -= 1
        num_printed_nums += 2
# 1 6 2 5 3 4 
# 5
# 1 5 2 4 3