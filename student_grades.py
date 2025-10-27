# student_grades.py

import sys
import click

grades = {
    "Ahmad": [90, 85, 80],
    "Sara": [70, 75, 68],
    "Omar": [50, 45, 60],
    "Lina": [95, 100, 92]
}

def get_average(student_name):
    """Return tuple (success: bool, message: str)."""
    if student_name not in grades:
        return False, f"Student '{student_name}' not found."
    scores = grades[student_name]
    avg = sum(scores) / len(scores)
    result = "Passed" if avg >= 60 else "Failed"
    return True, f"{student_name}: Average = {avg:.2f}, Result = {result}"

@click.command()
@click.argument("student")
def main(student):
    """Calculate a student's average grade and print the result."""
    ok, message = get_average(student)
    if ok:
        click.echo(message)
        sys.exit(0)   # success
    else:
        click.echo(f"❌ {message}", err=True)
        sys.exit(2)   # student not found (non-zero exit code)

if __name__ == "__main__":
    main()
