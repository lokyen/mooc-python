# Write your solution here

# Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

# Sample output
# Width: 10
# Height: 3
# ##########
# ##########
# ##########

width = int(input("Width: "))
height = int(input("Height: "))
count = 0

while count < height:
    print("#" * width)
    count += 1