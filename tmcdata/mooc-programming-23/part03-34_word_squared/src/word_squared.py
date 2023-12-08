# Write your solution here

def squared(string, integer):   
    total = 0
    text = (string*(integer*integer))
    while total < integer*integer:
        print(text[total:total+integer])
        total +=integer
if __name__ == "__main__":
    squared("ab", 3)