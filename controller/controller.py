import os
import ctypes

path = os.getcwd()

MODEL_C = ctypes.CDLL(os.path.join(path, "model/model.so"))

def getDisplay():
    MODEL_C.displayHello()