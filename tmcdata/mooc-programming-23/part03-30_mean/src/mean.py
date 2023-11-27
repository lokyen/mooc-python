# Please write a function named mean, which takes three integer arguments. The function should print out the arithmetic mean of the three arguments.
def mean(num_1, num_2, num_3):
    sum = num_1 + num_2 + num_3
    mean = (float)(sum / 3)
    print(mean)
# Write your code here

# Testing the function
if __name__ == "__main__":
    mean(1, 2, 3)