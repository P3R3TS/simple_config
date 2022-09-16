import configparser as _configparser
import os as _os
import _exception as _Error
from configparser import Error as __Error

class config:
    """
    calss class
    """
    def __init__(self, path: str = ".", filename: str = "config.ini") -> None:
        """
        
        """
        expansion = ".ini"
        if path == None:
            path = "."
        elif type(path) == str:
            self.checkPath()
            self.path = path
        else:
            raise _Error.incorrectPathError(path)
        if type(filename) == str:
            if (len(filename) - filename.find(expansion)) == len(expansion):
                self.filename = filename
            else:
                raise _Error.incorrectFileNameError(filename)
        else:
            raise _Error.configTypeError(filename, "str")
        try:
            self.config = _configparser.ConfigParser()
        except _Error as e:
            raise _Error.configError(e)
        self.__readConfig()
    
    def checkPath(self):
        if not list(self.path)[-1] == "/":
            _Error.incorrectPathError(self.path)
        counter = 0
        for elem in list(self.path):
            if elem == "/":
                counter = counter + 1
            elif counter < 2:
                counter = 0
            else:
                _Error.incorrectPathError(self.path)
        
    def __readConfig (self) -> None:
        """
        
        """
        if not _os.path.exists(self.fullpath()):
            self.__createConfig()

        try:
            self.config.read(self.fullpath())
        except _Error as e:
            raise _Error.configError(e)
        try:
            self.config = _configparser.ConfigParser()
        except _Error as e:
            raise _Error.configError(e)
        return self.config

    def __createConfig(self) -> None:
        """
        
        """
        if not self.fullpath() == False:
            if not _os.path.exists(self.path):
                _os.makedirs(self.path)
        self.__writeChangies()

    def __writeChangies(self) -> None:
        """
        
        """
        with open(self.fullpath(), "w") as config_file:
            try:
                self.config.write(config_file)
            except __Error as e:
                _Error.configError(e)
    
    def fullpath(self) -> None:
        """
        
        """
        if self.path == False:
            fullpath = self.filename
        else:
            fullpath = f"{self.path}/{self.filename}"
        return fullpath
    
    def delete(self, section: str = "DEFAULT", option: str = None) -> None:
        """
        
        """
        if not option == None:
            if type(section) == str:
                if (self.config.has_section(section)) or (section == "DEFAULT"):
                    if type(option) == str:
                        if self.config.has_option(section, option):
                            self.config.remove_option(section, option)
                            self.__writeChangies()
                        else:
                            raise _Error.notFound(option, "option")
                    else:
                        raise _Error.configTypeError(option, "str")
                else:
                    raise _Error.notFound(section, "section")
            else:
                raise _Error.configTypeError(section, "str")
        else:
            _Error.configError('the "option" cannot be "None"')

    def add(self, section: str = "DEFAULT", option: str = None, value: any = None) -> None:
        """
        
        """
        if not option == None:
            if type(section) == str:
                if type(option) == str:
                    if type(value) == str:
                        self.__addOption(section, option, value)
                    else:
                        raise _Error.configTypeError(value, "str")
                else:
                    raise _Error.configTypeError(option, "str")
            else:
                raise _Error.configTypeError(section, "str")
        else:
            _Error.configError('the "option" cannot be "None"')
    
    def __addOption(self, section: str, option: str, value: str) -> None:
        """
        
        """
        if not section == "DEFAULT":
            if not self.config.has_section(section):
                try:
                    self.config.add_section(section)
                except __Error as e:
                    _Error.configError(e)
        try:
            self.config.set(section, option, value)
        except __Error as e:
            _Error.configError(e)
        self.__writeChangies()
    
    def get(self, section: str = "DEFAULT", option: str = None) -> str:
        """
        
        """
        if not option == None:
            if type(section) == str:
                if type(option) == str:
                    if (self.config.has_section(section)) or (section == "DEFAULT"):
                        if self.config.has_option(section, option):
                            return self.config.get(section, option)
                        else:
                            raise _Error.notFound(option, "option")
                    else:
                        raise _Error.notFound(section, "section")
                else:
                    raise _Error.configTypeError(option, "str")
            else:
                raise _Error.configTypeError(section, "str")
        else:
            _Error.configError('the "option" cannot be "None"')
                    
    def remove(self) -> None:
        """
        
        """
        self.__writeChangies()

    def __del__(self) -> None:
        """
        
        """
        self.__writeChangies()

