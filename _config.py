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

    def set(self, section: str = "DEFAULT", option: str = None, value: any = None):
        if not option == None:
            if(type(value) == list):
                _str = " ".join(value)
            else:
                _str = value
            self.__addOption(section, option, _str, False)

    def add(self, section: str = "DEFAULT", option: str = None, value: any = None):
        if not option == None:
            if(type(value) == list):
                _str = " ".join(value)
            else:
                _str = value
            self.__addOption(section, option, _str, True)
    
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
    
    def get(self, section: str = "DEFAULT", option: str = None):
        if not option == None:
            if (self.config.has_section(section)) or (section == "DEFAULT"):
                if self.config.has_option(section, option):
                    _str = self.config.get(section, option)
                    if not len(_str.split()) == 1:
                        _str = _str.split()
                    return _str

    def remove(self) -> None:
        """
        
        """
        self.__writeChangies()

conf1 = config( 
    path = "./conf",
    filename = "Settings.ini"
)