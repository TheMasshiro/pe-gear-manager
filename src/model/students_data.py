import sqlite3
from pathlib import Path

script_dir = Path(__file__).parent.absolute()
database_file = script_dir / "data" / "students.db"


def create_table():
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
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return students


def insert_student(id, name, number, course, year, section):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Students (id, name, number, course, year, section) VALUES (?, ?, ?, ?, ?, ?)",
        (id, name, number, course, year, section),
    )
    conn.commit()
    conn.close()


def update_student(new_name, new_number, new_course, new_year, new_section):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Students SET name = ?, number = ?, course = ?, year = ?, section = ? WHERE id = ?",
        (new_name, new_number, new_course, new_year, new_section, id),
    )
    conn.commit()
    conn.close()


def delete_student(id):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def id_exists(id):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Students WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0


def name_exists(name):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Students WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0


create_table()
