import os
import platform

from ctypes import cdll

path = os.path.dirname(__file__)

sys = platform.system()

if sys == 'Windows':
    lib = cdll.LoadLibrary(f"{path}/build/bin/add_basic.dll")

i = lib.Add(6, 23)

print(i)