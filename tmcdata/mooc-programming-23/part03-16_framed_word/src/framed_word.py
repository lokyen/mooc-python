# Write your solution here

# Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

# If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

# Sample output
# Word: testing
# ******************************
# *          testing           *
# ******************************
# Sample output
# Word: python
# ******************************
# *           python           *
# ******************************


word = input("Word: ")
first_space = (28 - len(word)) // 2

if len(word) % 2 == 0:
    second_space = first_space
else:
    second_space = first_space + 1

print("*" * 30)
print("*" + " " * first_space + f"{word}" + " " * second_space + "*")
print("*" * 30)