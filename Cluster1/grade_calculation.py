# Student names and marks in CS, Math, and English
student_names = ["Anis", "Bella", "Charlie", "Gene", "Muhammad"]
cs = [95, 78, 85, 60, 92]
math = [88, 92, 75, 80, 78]
english = [90, 85, 92, 78, 88]

# Grade thresholds; minus 1 to include the limit in cutoff
a = 90 - 1
b = 80 - 1

# Iterating over students while checking grades
for i in range(len(student_names)):
    if any([cs[i] > a, math[i] > a, english[i] > a]) and all([cs[i] > b, math[i] > b, english[i] > b]):
        print(f"{student_names[i]} achieved the desired grades.")

# Problem:
# You have a list of student names. You have one list each for their marks in CS, Math and English.
# Hard code the values. Don't have to get it as an input.
# Grade A is score 90 or above
# Grade B 80 or above
# Fail is < 50
# Print the name of the students who got an A in all subjects or at least one A and the rest B.
# Try to use only one if statement.
