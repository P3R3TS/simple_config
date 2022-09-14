import configparser as _configparser
import os as _os

class config:
    """
    
    """
    def __init__(self, path: str = ".", filename: str = "config.ini"):
        """
        
        """
        self.path = path
        self.filename = filename
        self.config = _configparser.ConfigParser()
        self.__readConfig()
        
    def __readConfig (self) -> None:
        """
        
        """
        
        if not _os.path.exists(f"{self.path}/{self.filename}"):
            self.__createConfig()

        self.config = _configparser.ConfigParser()
        self.config.read(f"{self.path}/{self.filename}")
        print("read configuration file")
        return self.config

    def __createConfig(self) -> None:
        if not _os.path.exists(self.path):
            _os.makedirs(self.path)
        
        print ("create configuration file")
        self.__writeChangies()

    def __writeChangies(self) -> None:
        with open(f"{self.path}/{self.filename}", "w") as config_file:
            self.config.write(config_file)
    
    def fullpath(self) -> None:
        fullpath = f"{self.path}/{self.filename}"
        return fullpath
    
    def delete(self, section: str = "DEFAULT", option: str = None, value: any = None, all: bool = False):
        if (not option == None) and (type(option) == str) and self.config.has_option(section, option):
            if (self.config.has_section(section)) or (section == "DEFAULT"):
                if all == True:
                    self.config.remove_option(section, option)
                elif value == None:
                    _str = self.get(section, option)
                    if not type(_str) == list:
                        _str = _str.split()
                    if (len(_str) <= 1):
                        self.config.remove_option(section, option)
                    else:
                        del _str[len(_str)-1]
                        _str = " ".join(_str)
                        self.set(section, option, _str)
                else:
                    _str = self.get(section, option)
                    if not type(_str) == list:
                        _str = _str.split()
                    if str(value) in _str:
                        _str.remove(str(value))
                    if (len(_str) < 1):
                        self.config.remove_option(section, option)
                    else:
                        _str = " ".join(_str)
                        self.set(section, option, _str)
        self.__writeChangies()

    def set(self, section: str = "DEFAULT", option: str = None, value: any = None):
        if not option == None:
            if(type(value) == list):
                _str = " ".join(value)
            else:
                _str = value
            self.__addOption(section, option, str(_str), False)

    def add(self, section: str = "DEFAULT", option: str = None, value: any = None):
        if not option == None:
            if(type(value) == list):
                _str = " ".join(value)
            else:
                _str = value
            self.__addOption(section, option, str(_str), True)
    
    def __addOption(self, section: str, option: str, value: str, arr: bool):
        if not section == "DEFAULT":
            if not self.config.has_section(section):
                self.config.add_section(section)
        if (self.config.has_option(section, option)) and (arr == True):
            _str = self.config.get(section, option)
            _str = _str.split()
            _str.append(value)
            _str = " ".join(_str)
            self.config.set(section, option, _str)
        else:
            self.config.set(section, option, value)
        self.__writeChangies()
    
    def get(self, section: str = "DEFAULT", option: str = None, returnType: str = None):
        if not option == None:
            if (self.config.has_section(section)) or (section == "DEFAULT"):
                if self.config.has_option(section, option):
                    _str = self.config.get(section, option)
                    if returnType == None:
                        if not len(_str.split()) == 1:
                            _str = _str.split()
                    elif returnType == "list":
                        _str = _str.split()
                    else:
                        pass
                    return _str

    def remove(self) -> None:
        """
        
        """
        self.__writeChangies()