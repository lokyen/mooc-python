# Write your solution here

first = input("Please type in the 1st word: ")
second = input("Please type in the 2nd word: ")
if first > second:
    print(f"{first} comes alphabetically last.")
elif second > first:
    print(f"{second} comes alphabetically last.")
elif first == second:
    print("You gave the same word twice.")