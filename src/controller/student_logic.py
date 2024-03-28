"""

Module : student_logic.py

This module acts as an intermediary between the view.py and student_data.py modules.
It handles the data flow and operations related to student information.

"""

from tkinter.constants import END
from datetime import datetime
from src.model import (
    fetch_students,
    insert_student,
    update_student,
    delete_student,
    student_id_exists,
    student_name_exists,
)


def student_id_record(id):
    # Checks if a student id already exists in the database
    return student_id_exists(id)


def student_name_record(name):
    # Checks if a student name already exists in the database
    return student_name_exists(name)


def autofill_helper_fill(
    id_number,
    student_name,
    student_number,
    student_course,
    student_year,
    student_section,
    tk,
):
    student_records = fetch_students()
    for row in student_records:
        if row[0] == id_number.get():
            student_name.delete(0, tk.END)
            student_name.insert(0, row[1])
            student_number.delete(0, tk.END)
            student_number.insert(0, row[2])
            student_course.delete(0, tk.END)
            student_course.insert(0, row[3])
            student_year.set(row[4])
            student_section.delete(0, tk.END)
            student_section.insert(0, row[5])


def autofill_helper_clear(
    id_number,
    student_name,
    student_number,
    student_course,
    student_year,
    student_section,
    tk,
):
    id_number.delete(0, tk.END)
    student_name.delete(0, tk.END)
    student_number.delete(0, tk.END)
    student_course.delete(0, tk.END)
    student_year.set("")
    student_section.delete(0, tk.END)


def sign_up_insert_data(
    id_number,
    student_name,
    student_number,
    student_course,
    student_year,
    student_section,
):
    id = id_number.get()
    name = student_name.get().title()
    number = student_number.get()
    course = student_course.get().upper()
    year = student_year.get()
    section = student_section.get().upper()
    insert_student(id, name, number, course, year, section)


def student_tree_helper(tree):
    student_records = fetch_students()
    time_now = datetime.now()
    sign_in_time = time_now.strftime("%I:%M %p")
    tree.delete(*tree.get_children())
    for row in student_records:
        course_year_section = f"{row[3]} - {row[4]}{row[5]}"
        tree.insert("", END, value=(row[0], row[1], course_year_section, sign_in_time))
