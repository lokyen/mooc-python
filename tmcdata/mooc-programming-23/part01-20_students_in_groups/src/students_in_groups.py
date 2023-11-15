# Write your solution here

# Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.


total_students = int(input("How many students in the course? "))
people_per_group = int(input("Desired group size? "))
if total_students % people_per_group != 0:
    group_total = total_students // people_per_group
    group_total += 1
else:
    group_total = total_students // people_per_group

print(f"Number of groups formed: {group_total}")