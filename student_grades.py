# student_grades.py

import click

grades = {
    "Ahmad": [90, 85, 80],
    "Sara": [70, 75, 68],
    "Omar": [50, 45, 60],
    "Lina": [95, 100, 92]
}

def get_average(student_name):
    if student_name not in grades:
        click.echo(f"❌ Student '{student_name}' not found.")
        return
    scores = grades[student_name]
    avg = sum(scores) / len(scores)
    result = "✅ Passed" if avg >= 60 else "❌ Failed"
    click.echo(f"{student_name}: Average = {avg:.2f}, Result = {result}")

@click.command()
@click.argument("student")
def main(student):
    """Calculate a student's average grade and print the result."""
    get_average(student)

if __name__ == "__main__":
    main()
