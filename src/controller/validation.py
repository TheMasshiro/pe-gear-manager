"""

Module : validation.py

validation.py is used to validate
the from libvalidation.so.
It checks if the ID, name,
phone number, course and
section are valid or not

"""
import ctypes
import os

# Get the current working dictionary
path = os.getcwd()

# Load shared library libvalidation.so
library = ctypes.CDLL(os.path.join(path, "src/model/libvalidation.so"))

# Check if the details are valid or not
# Returns True if valid
# Returns False if invalid
library.validate_id_number.argtypes = [ctypes.c_char_p]
library.validate_id_number.restype = ctypes.c_bool

library.validate_name.argtypes = [ctypes.c_char_p]
library.validate_name.restype = ctypes.c_bool

library.validate_phone_number.argtypes = [ctypes.c_char_p]
library.validate_phone_number.restype = ctypes.c_bool

library.validate_course.argtypes = [ctypes.c_char_p]
library.validate_course.restype = ctypes.c_bool

library.validate_section.argtypes = [ctypes.c_char_p]
library.validate_section.restype = ctypes.c_bool


def validate_id(id_number):
    """ Function to validate ID """
    student_id = ctypes.c_char_p(id_number.encode("utf-8"))
    is_valid = library.validate_id_number(student_id)
    return bool(is_valid)


def validate_name(name):
    """ Function to validate name """
    student_name = ctypes.c_char_p(name.encode("utf-8"))
    is_valid = library.validate_name(student_name)
    return bool(is_valid)


def validate_phone_number(number):
    """ Function to validate phone number """
    phone_number = ctypes.c_char_p(number.encode("utf-8"))
    is_valid = library.validate_phone_number(phone_number)
    return bool(is_valid)


def validate_course(course):
    """ Function to validate course """
    student_course = ctypes.c_char_p(course.encode("utf-8"))
    is_valid = library.validate_course(student_course)
    return bool(is_valid)


def validate_section(section):
    """ Function to validate section """
    student_section = ctypes.c_char_p(section.encode("utf-8"))
    is_valid = library.validate_section(student_section)
    return bool(is_valid)
