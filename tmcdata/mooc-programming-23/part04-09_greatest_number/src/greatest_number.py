# Write your solution here
# Please write a function named  greatest_number, which takes three arguments. The function returns the greatest in value of the three
def greatest_number(num_1, num_2, num_3):
    num = []
    num.append(num_1)
    num.append(num_2)
    num.append(num_3)
    return max(num)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)