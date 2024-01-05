# Write your solution here

# Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.
def spruce(size):
    print("a spruce!")
    i = 1
    while i <= size:
        empty = size - i
        stars = 2 * i - 1
        print(" " * empty + "*" * stars)
        i += 1
    print(" " * (size - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)