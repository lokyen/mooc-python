# Write your solution here

year = int(input("Year: "))
next_leap = year
while True:
    next_leap += 1
    if next_leap % 4 == 0:
        if next_leap % 400 == 0 and next_leap % 100 == 0:
            print(f"The next leap year after {year} is {next_leap}")
            break
        elif next_leap % 400 != 0 and next_leap % 100 != 0:
            print(f"The next leap year after {year} is {next_leap}")
            break

    