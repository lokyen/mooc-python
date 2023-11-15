# Write your solution here

# Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.

# Sample output
# PIN: 3245
# Wrong
# PIN: 1234
# Wrong
# PIN: 0000
# Wrong
# PIN: 4321
# Correct! It took you 4 attempts

# If the user gets it right on the first try, the program should print out something a bit different:

# Sample output
# PIN: 4321
# Correct! It only took you one single attempt!

attempts = 0

while True:
    pin_num = int(input("Pin: "))
    attempts += 1
    if(pin_num == 4321):
        if(attempts == 1):
            print("Correct! It only took you one single attempt!")
            break
        print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong") 