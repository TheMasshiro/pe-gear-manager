"""

Module : student_data.py

This module handles data manipulation operations for the student database.
It provides functions to create the database table, fetch student records,
insert new student records, update existing records, delete records,
and check if a student ID or name already exists in the database.

"""

import sqlite3
from pathlib import Path

script_dir = Path(__file__).parent.absolute()
database_file = script_dir / "data" / "students.db"


def create_table():
    # Create the Students table in the database if it doesn't already exist
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Students
            (
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   number TEXT,
                   course TEXT,
                   year TEXT,
                   section TEXT
                   )
                   """
    )
    conn.commit()
    conn.close()


def fetch_student():
    # Retrieve all student records from the database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return students


def insert_student(id, name, number, course, year, section):
    # Insert a new student record into the database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Students (id, name, number, course, year, section) VALUES (?, ?, ?, ?, ?, ?)",
        (id, name, number, course, year, section),
    )
    conn.commit()
    conn.close()


def update_student(new_name, new_number, new_course, new_year, new_section):
    # Update an existing student record in the database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Students SET name = ?, number = ?, course = ?, year = ?, section = ? WHERE id = ?",
        (new_name, new_number, new_course, new_year, new_section, id),
    )
    conn.commit()
    conn.close()


def delete_student(id):
    # Delete a student record from the database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def id_exists(id):
    # Check if a student id already exists in the table
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Students WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0


def name_exists(name):
    # Check if a student name already exists in the table
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Students WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0


create_table()
