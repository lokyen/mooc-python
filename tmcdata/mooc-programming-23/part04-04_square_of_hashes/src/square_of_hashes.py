# Copy here code of line function from previous exercise
def line(number, str_arg):
    if(str_arg == ""):
        str_arg = "*"
    print(str_arg[0] * number)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    count = size
    while count > 0:
        line(size, "#")
        count -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
