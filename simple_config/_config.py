import configparser as _Configparser
import os as _Os
from . import _exception as _Error
from configparser import Error as __Error
from pathlib import Path

class config:
    """
        >>> Main config class
        >>> Initialization simple config
        >>> path - Config directory
        >>> filename - Name of the configuration file
        >>> Example:
        >>> config = config(path = "./advancedSettings/Settings", filename = "configuration.ini")
    """
    def __init__(self, path: str = None, filename: str = "config.ini") -> None:
        
        expansion = ".ini"
        if path == None:
            self.path = None
        elif type(path) == str:
            self.path: Path = Path(path)
        else:
            raise _Error.incorrectPathError(path)
        if type(filename) == str:
            if (len(filename) - filename.find(expansion)) == len(expansion):
                self.filename: Path = Path(filename)
            else:
                raise _Error.incorrectFileNameError(filename)
        else:
            raise _Error.configTypeError(filename, "str")
        try:
            self.config = _Configparser.ConfigParser()
        except _Error as e:
            raise _Error.configError(e)
        self.__readConfig()
        
    def __readConfig (self) -> None:
        """
            >>> read config method.
            >>> Checking if a configuration file exists, if not, then creating a configuration file.
            >>> Reading configuration file.
            >>> Return configuraion file
        """
        if not _Os.path.exists(self.fullpath()):
            self.__createConfig()
        try:
            self.config.read(self.fullpath())
        except _Error as e:
            raise _Error.configError(e)
        try:
            self.config = _Configparser.ConfigParser()
        except _Error as e:
            raise _Error.configError(e)
        return self.config

    def __createConfig(self) -> None:
        """
            >>> Create configuration file.
            >>> Checking whether the necessary directory exists, if not, creating directory.
            >>> Starting write changing function.
        """
        if not self.path == None:
            """print(_Os.path.exists(str(self.path)))
            if _Os.path.exists(str(self.path)) == False:"""
            
            _Os.makedirs(str(self.path), exist_ok = True)
        self.__writeChangies()

    def __writeChangies(self) -> None:
        """
            open necessary file
        """
        
        with open(self.fullpath(), "w") as config_file:
            try:
                self.config.write(config_file)
            except __Error as e:
                _Error.configError(e)
    
    def fullpath(self) -> str:
        """
            return string full path with path and file name
        """
        if self.path == None:
            fullpath = str(self.filename)
        else:
            fullpath = str(self.path/self.filename)
        return fullpath
    
    def delete(self, section: str = "DEFAULT", option: str = None) -> None:
        """
            >>> delete option function.
            >>> example:
            >>> config.delete(section = "Global settins", option = "Time to answer")
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
            >>> add function.
            >>> example:
            >>> config.add(section = "Global settins", option = "Time to answer", value = 1000)
        """
        if not option == None:
            if type(section) == str:
                if type(option) == str:
                    if type(value) == str:
                        self.__addOption(section, option, value)
                    else:
                        if type(value) in [int, float, complex]:
                            value = str(value)
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
            Add option function
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
    
    def get(self, section: str = "DEFAULT", option: str = None, gettingtype: str  = "str"):
        """
            >>> add function.
            >>> gettingtype can be str, int, float and complex
            >>> example:
            >>> returned = config.get(section = "Global settins", option = "Time to answer")
            >>> returned is 1000
        """
        if not option == None:
            if type(section) == str:
                if type(option) == str:
                    if (self.config.has_section(section)) or (section == "DEFAULT"):
                        if self.config.has_option(section, option):
                            _str = self.config.get(section, option)
                            if gettingtype == "str":
                                return _str
                            elif gettingtype == "int":
                                return int(_str)
                            elif gettingtype == "float":
                                return float(_str)
                            elif gettingtype == "complex":
                                return complex(_str)
                            else:
                                _Error.configError('getting rype aruments can be only "str", "float" and "complex"')
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