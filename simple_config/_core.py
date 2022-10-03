from io import TextIOWrapper

class core:
    def __INIT__(self):
        self.section = "[DEFAULT]"

    def parse(self, file: TextIOWrapper):
        line = file.readline()
        
        while True:
            line = file.readline()
            if not line:
                break
            
    def _checkCorrectNameSection(self, line):
        if len(line.split()) == 1:
            if (list(line)[0] == "[") and (list(line)[-1] == "]"):
                line = list(line)
                line.remove("[")
                line.remove("]")
                line = "".join(line)
            list(line).count("[")
            return line
        else: print('duuds')

    def write(self, file: TextIOWrapper):
        pass

####### Tested parse alorithm
file = open('config.ini', 'r')
try:
    line1 = file.readline()
    
finally:
    file.close()

"""
Parse algorithm:
    before start:
        1. line = readline
        2. if line == Section # Section mask: [*String*] else error
        3. create dict {line = none}
    start parse:
        1. line = readline
        2. if not line == None: else return dict 
        3. if line == Option # Option mask: *String* = *String*. Option = Param
        4. option = option
        5. param = param
        6. add to dict {Section = {option_1 = param_1, ...}, ...}
        7. return to 1

Write algorithm:
    before start:
        1. Check correctly dict: str = {section_1 = {option_1 = param_1, ..., , option_n = param_n}, ..., section_n = {option_1 = param_1, ..., option_n = param_n}}
    start write:
        1. n = 0
        2. n ++
        3. if not dect[n] == None: else return finish
        4. writeline f'[{dict[n]}]'
        5. n2 = 0
        6. n2 ++
        7. if not dict[n[n2]] == None: else return to 2
        8. writeline  f'{dict[n[n2]]}'
        9. return to 6
"""