# Write your solution here

print("Person 1:")
name_one = input("Name: ")
age_one = int(input("Age: "))
print("Person 2:")
name_two = input("Name: ")
age_two = int(input("Age: "))
if age_one > age_two:
    print(f"The elder is {name_one}")
elif age_two > age_one:
    print(f"The elder is {name_two}")
else:
    print(f"{name_one} and {name_two} are the same age")