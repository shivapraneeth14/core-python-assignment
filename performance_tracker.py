def calculate_average(marks):
    return round(sum(marks) / len(marks), 2)


def get_student_averages(students):
    averages = {}
    for student, marks in students.items():
        averages[student] = calculate_average(marks)
    return averages


def find_top_performer(averages):
    return max(averages, key=averages.get)


students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

averages = get_student_averages(students)
top_student = find_top_performer(averages)

print("Average Marks:", averages)
print("Top Performer:", top_student)
