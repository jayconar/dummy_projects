# Student names and marks
students = ["Flynn", "Brad", "Kiran", "Svetlana", "Nadiya"]
scores = [75, 48, 60, 30, 85]

# Cutoff score
cutoff = 50

# Lists to store passed students and failed students
passed_students = []
failed_students_count = 0

# Iterate over the students and check if they passed
for i in range(len(students)):
    if scores[i] >= cutoff:
        passed_students.append(f"{students[i]}:{scores[i]}")
    else:
        failed_students_count += 1

# Printing the list of passed students
print("List of passed students:")
for student in passed_students:
    print(student)

# Printing the number of students who failed
print(f"\nNumber of students who failed: {failed_students_count}")
