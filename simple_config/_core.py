from io import TextIOWrapper

class core:
    def __init__(self):
        self.sectionDeffault = "DEFAULT"

    def parse(self, file: TextIOWrapper):
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
            param = self.configDict[section][option]
        except KeyError:
            pass
            ## need to add exception
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
        if section == None:
            if self.has_section(self.sectionDeffault) == False:
                self.configDict[self.sectionDeffault] = {}
            self.configDict[self.sectionDeffault][option] = value
        else:
            self.configDict[section][option] = value
        return True

    def write(self, file: TextIOWrapper):
        for key, value in self.configDict.items():
            file.write(f'[{key}]\n')
            for key, Value in value.items():
                file.write(f'{key} = {Value}\n')
            file.write('\n')

        

####### Tested alorithm

conf = core()

file = open("config.ini", 'r')
dict1 = conf.parse(file)
file.close()

param = conf.get("CONFIGS", "set1")
request1 = conf.has_option("CONFIGS", "set1")
request2 = conf.has_section("CONFIGS")
request3 = conf.add_section("CONFIGS22")
request4 = conf.has_section("CONFIGS22")
request5 = conf.set(option = "fake", value = "True")

file = open("config.ini", 'w')
conf.write(file)
file.close()

print(dict1)
print(param)
print(request1)
print(request2)
print(request3)
print(request4)

"""
Need to add exceptions, create testes and import to main _config script
"""