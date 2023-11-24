# Student names and marks
students = ["Flynn", "Brad", "Sofia", "Alisha", "Nadia"]
scores = [75, 48, 60, 30, 85]

cutoff = 50  # Cutoff score

# Lists to store passed students and failed students
passed_students = []
failed_students_count = 0

# Iterating over the students and checking if they passed
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

# Problem:
# You have a list of student names and another list with their marks in a subject.
# Hard code the values. Don't have to get it as an input
# Pass mark is 50.
# Print a new list with all the students with pass marks along with their mark in the format name:mark.
# Also print the number of students who've failed.
