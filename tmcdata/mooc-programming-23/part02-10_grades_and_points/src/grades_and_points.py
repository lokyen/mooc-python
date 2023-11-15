# Write your solution here

points = int(input("How many points [0-100]: "))
if points < 0:
    grade = "impossible!"
elif points >= 0 and points <= 49:
    grade = "fail"
elif points >= 50 and points <= 59:
    grade = str(1)
elif points >= 60 and points <= 69:
    grade = str(2)
elif points >= 70 and points <= 79:
    grade = str(3)
elif points >= 80 and points <= 89:
    grade = str(4)
elif points >= 90 and points <= 100:
    grade = str(5)
else:
    grade = "impossible!"
print(f"Grade: {grade}")