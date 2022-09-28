
from ctypes import Union
from io import TextIOWrapper
import io


class core:
    def __INIT__(self):
        self.section = "[DEFAULT]"

    def parse(self, file = open("config.ini", "r")):
        while True:
            line = file.readline()
            if not line:
                break
            

    def write(self, file = open("config.ini", "w")):
        pass

