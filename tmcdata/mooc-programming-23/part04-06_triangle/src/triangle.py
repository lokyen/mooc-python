# Copy here code of line function from previous exercise
def line(number, str_arg):
    if(str_arg == ""):
        str_arg = "*"
    print(str_arg[0] * number)

def triangle(size):
    # You should call function line here with proper parameters
    num = 1
    while num <= size:
        line(num, "#")
        num += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
