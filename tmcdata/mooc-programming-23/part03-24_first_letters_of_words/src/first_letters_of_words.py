# Write your solution here

# Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a sentence: Humpty Dumpty sat on a wall
# H
# D
# s
# o
# a
# w

word = input("Please type in a sentence: ")
word_list = word.split()

i = 0
while i < len(word_list):
    print(word_list[i][0]);
    i += 1