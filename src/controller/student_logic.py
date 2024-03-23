from src.model import (
    fetch_student,
    insert_student,
    delete_student,
    id_exists,
    name_exists,
)


def insert_data(id, name, number, course, year, section):
    insert_student(id, name, number, course, year, section)


def id_data_exists(id):
    return id_exists(id)


def name_data_exists(name):
    return name_exists(name)
