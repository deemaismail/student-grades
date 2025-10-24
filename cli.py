import click
import json
import os
import logging
# إعداد نظام التسجيل (Logging)
logging.basicConfig(
    filename="student_grades.log",  # اسم ملف السجل
    level=logging.INFO,             # مستوى التفاصيل (INFO, WARNING, ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

DATA_FILE = "students.json"

def load_students():
    """تحميل بيانات الطلاب من الملف"""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_students(students):
    """حفظ بيانات الطلاب في الملف"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

@click.group()
def cli():
    """برنامج بسيط لإدارة علامات الطلاب."""
    pass


@cli.command()
@click.argument('name')
@click.argument('grade', type=float)
def add_student(name, grade):
    """إضافة طالب وعلامته."""
    students = load_students()
    students[name] = grade
    save_students(students)
    logging.info(f"تمت إضافة الطالب {name} بعلامة {grade}")

    click.echo(f"✅ تمت إضافة الطالب {name} بعلامة {grade}")


@cli.command()
def list_students():
    """عرض جميع الطلاب وعلاماتهم."""
    students = load_students()
    logging.info("تم تنفيذ أمر عرض الطلاب.")

    if not students:
        click.echo("📭 لا يوجد طلاب بعد.")
    else:
        for name, grade in students.items():
            click.echo(f"{name}: {grade}")


@cli.command()
def calculate_average():
    """حساب المعدل العام للطلاب."""
    students = load_students()
    if not students:
        logging.info(f"تم حساب المعدل العام للطلاب ({len(students)} طالب).")

        click.echo("❌ لا يوجد طلاب لحساب المعدل.")
    else:
        avg = sum(students.values()) / len(students)
        logging.info(f"تم حساب المعدل العام ({avg:.2f}) لعدد {len(students)} طلاب.")
        click.echo(f"📊 المعدل العام: {avg:.2f}")


if __name__ == "__main__":
    cli()
