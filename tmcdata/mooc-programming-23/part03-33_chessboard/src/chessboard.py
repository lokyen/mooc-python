# Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:

# Write your solution here
def chessboard(dimensions):
    row = dimensions
    column = dimensions
    for i in range(row):
        if i % 2 == 0: 
            # if even print 101 pattern
            for j in range(column):
                if j % 2 == 0:
                    print(1, end="")
                else:
                    print(0, end="")
            print()
        else: 
            # print 010 for odd
            for j in range(column):
                if j % 2 == 0:
                    print(0, end="")
                else:
                    print(1, end="")
            print()
            
# Testing the function
if __name__ == "__main__":
    chessboard(3)
