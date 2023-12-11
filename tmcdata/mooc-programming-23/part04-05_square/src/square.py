# Copy here code of line function from previous exercise
def line(number, str_arg):
    if(str_arg == ""):
        str_arg = "*"
    print(str_arg[0] * number)
    
def square(size, character):
    # You should call function line here with proper parameters
    num = size
    while num > 0:
        line(size, character)
        num -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "+")