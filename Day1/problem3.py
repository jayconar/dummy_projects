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
