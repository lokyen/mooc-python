# Write your solution here

# Please write a program which asks the user for a number of days. The program then prints out the number of seconds in the amount of days given.

days = int(input("How many days? "))
seconds_in_days = 60 * 60 * 24 * days
print(f"Seconds in that many days: {seconds_in_days}")