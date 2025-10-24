# student_grades.py

grades = {
    "Ahmad": [90, 85, 80],
    "Sara": [70, 75, 68],
    "Omar": [50, 45, 60],
    "Lina": [95, 100, 92]
}

for student, scores in grades.items():
    avg = sum(scores) / len(scores)
    if avg >= 60:
        result = "Passed"
    else:
        result = "Failed"
    print(f"{student}: Average = {avg:.2f}, Result = {result}")
