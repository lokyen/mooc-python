# Write your solution here

# Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

# Some examples of expected behaviour:

# Sample output
# Please type in string 1: hey
# Please type in string 2: hiya
# hiya is longer
# Sample output
# Please type in string 1: howdy doody
# Please type in string 2: hola
# howdy doody is longer

string_one = input("Please type in string 1: ")
string_two = input("Please type in string 2: ")

if len(string_one) > len(string_two):
    print(f"{string_one} is longer")
elif len(string_one) < len(string_two):
    print(f"{string_two} is longer")
else:
    print("The strings are equally long")