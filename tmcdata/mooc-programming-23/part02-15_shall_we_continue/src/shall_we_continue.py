# Write your solution here

# Let's create a program along the lines of the example above. 
# This program should print out the message "hi" and then ask "Shall we continue?" 
# until the user inputs "no". Then the program should print out "okay then" and finish.
# Please have a look at the example below.

while True:
    print("hi")
    decision = input("Shall we continue? ")
    if decision == 'no':
        break
print("okay then")