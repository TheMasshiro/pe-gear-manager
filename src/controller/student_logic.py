"""

Module : student_logic.py

This module acts as an intermediary between the view.py and student_data.py modules.
It handles the data flow and operations related to student information.

"""

from src.model import (
    fetch_student,
    insert_student,
    delete_student,
    id_exists,
    name_exists,
)


def insert_data(id, name, number, course, year, section):
    # Insert a new student record into the database
    insert_student(id, name, number, course, year, section)


def id_data_exists(id):
    # Checks if a student id already exists in the database
    return id_exists(id)


def name_data_exists(name):
    # Checks if a student name already exists in the database
    return name_exists(name)
