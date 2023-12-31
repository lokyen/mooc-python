# Write your solution here

# Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e or o.

# You may assume the input will be in lowercase entirely. Have a look at the examples below.

# Sample output
# Please type in a string: hello there
# a not found
# e found
# o found
# Sample output
# Please type in a string: hiya
# a found
# e not found
# o not found

word = input("Please type in a string: ")
vowels = ["a", "e", "o"]
iteration = 0

while iteration < len(vowels):
    if vowels[iteration] in word:
        print(f"{vowels[iteration]} found")
    else:
        print(f"{vowels[iteration]} not found") 
    iteration += 1