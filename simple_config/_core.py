from io import TextIOWrapper
from . import _exception as _Error

class core:
    def __init__(self):
        self.sectionDeffault = "DEFAULT"

    def read(self, file: TextIOWrapper):
        if not type(file) == TextIOWrapper:
            raise _Error.configError('file can be only io.TextIOWrapper type')
        self.configDict = {}
        while True:
            line = file.readline()
            if not self._checkCorrectNameSection(line) == None:
                nameSection = self._checkCorrectNameSection(line)
                self.configDict[nameSection] = {}
            if not self._returnOption(line) == None:
                self.configDict[nameSection][self._returnOption(line)] = self._returnParam(line)
                    
            if not line:
                break

        return self.configDict
    
    def _returnOption(self, line):
        if len(line.split()) > 2:
            if line.split()[1] == "=":
                option = line.split()[0]
                option = "".join(option)
                return option

    def _returnParam(self, line):
        if len(line.split()) > 2:
            if line.split()[1] == "=":

                param = line.split()
                del param[0:2]
                param = " ".join(param)
                return param
            

    def _checkCorrectNameSection(self, line):
        if len(line.split()) == 1:
            if (list(line)[0] == "[") and (list(line)[-2] == "]"):
                line = list(line)
                del line[0]
                del line[-2:-1]
                line = "".join(line)
                line = line.strip('\n')
                line = line.strip('\t')
            return line
        else: return None
    
    def get(self, section: str, option: str):
        try:
            try:
                self.configDict[section]
            except KeyError:
                raise _Error.sectionError(section)
            param = self.configDict[section][option]
        except KeyError:
            raise _Error.sectionError(option, section)
        else:
            return param
        
    def has_option(self, section: str, option: str):
        try:
            self.configDict[section][option]
        except KeyError:
            return False
        return True
    
    def has_section(self, section: str):
        try:
            self.configDict[section]
        except KeyError:
            return False
        return True
    
    def add_section(self, section: str):
        self.configDict[section] = {}
        return True
    
    def set(self, section: str = None, option: str = None, value: str = None):
        if option == None:
            raise _Error.configError('option can\'t be None')
        if value == None:
            raise _Error.configError('value can\'t be None')
        if section == None:
            if self.has_section(self.sectionDeffault) == False:
                self.configDict[self.sectionDeffault] = {}
            self.configDict[self.sectionDeffault][option] = value
        else:
            try:
                self.configDict[section][option] = value
            except KeyError:
                raise _Error.optionError(option, section)
        return True

    def write(self, file: TextIOWrapper):
        for key, value in self.configDict.items():
            file.write(f'[{key}]\n')
            try:
                for key, Value in value.items():
                    file.write(f'{key} = {Value}\n')
                file.write('\n')
            except AttributeError:
                pass
    
    def remove_option(self, section, option):
        if self.has_section == False:
            raise _Error.sectionError(section)
        if self.has_section == False:
            raise _Error.optionError(option, section)
        tempDict = self.configDict[section]
        self.configDict[section] = tempDict.pop(option)

        if not type(self.configDict[section]) == dict:
            self.configDict.pop(section)
            