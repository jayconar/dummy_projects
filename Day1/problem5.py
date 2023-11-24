def get_department_data(department):
    input_str = input(f"Enter the number of students and their marks in {department} (comma-separated): ")
    data = input_str.split(',')
    total_students = int(data[0])
    marks = [int(mark) for mark in data[1:]] if len(data) > 1 else []
    return total_students, marks


def top_3_marks(marks):
    sorted_marks = sorted(marks, reverse=True)
    return sorted_marks[:3]


def average_passing_mark(marks, pass_mark=50):
    passing_marks = [mark for mark in marks if mark >= pass_mark]
    return sum(passing_marks) / len(passing_marks) if passing_marks else 0


departments = ["CSE", "IT", "ECE"]
dept_data = {}

for dept in departments:
    students, scores = get_department_data(dept)
    dept_data[dept] = {'number_of_students': students, 'marks': scores}

print("\nTop 3 marks in each department:")
for dept, record in dept_data.items():
    top_3 = top_3_marks(record['marks'])
    print(f"{dept}: {top_3}")

all_scores = [mark for data in dept_data.values() for mark in data['marks']]
top_3_all_departments = top_3_marks(all_scores)
print(f"\nTop 3 marks across all departments: {top_3_all_departments}")

print("\nAverage mark of passing students:")
dept_avg_marks = {}
for dept, record in dept_data.items():
    avg_mark = average_passing_mark(record['marks'])
    dept_avg_marks[dept] = avg_mark
    print(f"{dept}: {avg_mark:.2f}")

best_avg_dept = max(dept_avg_marks, key=dept_avg_marks.get)
least_failed_dept = min(dept_data, key=lambda department: dept_data[department]['marks'].count(0))

print(f"\nDepartment with the best average mark: {best_avg_dept}")
print(f"Department with the least number of failed students: {least_failed_dept}")
