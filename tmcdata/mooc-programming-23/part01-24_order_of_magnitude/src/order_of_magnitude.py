# Write your solution here

# Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number according to the following examples.

# Sample output
# Please type in a number: 950
# This number is smaller than 1000
# Thank you!
# Sample output
# Please type in a number: 59
# This number is smaller than 1000
# This number is smaller than 100
# Thank you!

num = int(input("Please type in a number: "))
if num < 1000:
    print("This number is smaller than 1000")
    if num < 100:
        print("This number is smaller than 100")
        if num < 10:
            print("This number is smaller than 10")
print("Thank you!")