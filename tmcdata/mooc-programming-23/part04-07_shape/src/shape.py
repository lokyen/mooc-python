# Copy here code of line function from previous exercise and use it in your solution
def line(number, str_arg):
    if(str_arg == ""):
        str_arg = "*"
    print(str_arg[0] * number)

def shape(size_triangle, letter, height, filler_char):
    num = 1
    while num <= size_triangle:
        line(num, letter)
        num += 1
    num = 1
    while num <= height:
        line(size_triangle, filler_char)
        num += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")