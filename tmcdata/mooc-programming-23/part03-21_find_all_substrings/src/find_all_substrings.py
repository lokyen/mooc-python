# Write your solution here

# Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

word = input("Please type in a word: ")
character = input("Please type in a character: ")

while True:
    if len(word) == 0:
        break
    index = word.find(character)
    if index > -1:
        if len(word) < 3:
            break
        else:
            if len(word[index:]) < 3:
                break 
            print(word[index: (index + 3)])
            index += 1
            word = word[index: ]
    else:
        break