import ctypes
import os

path = os.getcwd()
library = ctypes.CDLL(os.path.join(path, "src/model/libvalidation.so"))

library.validate_id_number.argtypes = [ctypes.c_char_p]
library.validate_id_number.restype = ctypes.c_bool

library.validate_phone_number.argtypes = [ctypes.c_char_p]
library.validate_phone_number.restype = ctypes.c_bool


def validate_id(id_number):
    student_id = ctypes.c_char_p(id_number.encode("utf-8"))
    is_valid = library.validate_id_number(student_id)
    return bool(is_valid)


def validate_phone_number(number):
    phone_number = ctypes.c_char_p(number.encode("utf-8"))
    is_valid = library.validate_phone_number(phone_number)
    return bool(is_valid)
