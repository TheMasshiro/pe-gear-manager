from src.model import fetch_student, insert_student, delete_student, id_exists


def insert_data(id, name, number, course, year, section):
    insert_student(id, name, number, course, year, section)
