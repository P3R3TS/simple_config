import configparser as _configparser
import os as _os

class config:
    """
    calss class
    """
    def __init__(self, path: str = ".", filename: str = "config.ini"):
        """
        
        """
        if path == False:
            path = "."
        self.path = path
        self.filename = filename
        self.config = _configparser.ConfigParser()
        self.__readConfig()
        
    def __readConfig (self) -> None:
        """
        
        """

        if not _os.path.exists(self.fullpath()):
            self.__createConfig()

        self.config.read(self.fullpath())
        self.config = _configparser.ConfigParser()
        print("read configuration file")
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
            self.config.write(config_file)
    
    def fullpath(self) -> None:
        """
        
        """
        if self.path == False:
            fullpath = self.filename
        else:
            fullpath = f"{self.path}/{self.filename}"
        return fullpath
    
    def delete(self, section: str = "DEFAULT", option: str = None):
        """
        
        """
        if not option == None:
            if type(section) == str:
                if (self.config.has_section(section)) or (section == "DEFAULT"):
                    if type(option) == str:
                        if self.config.has_option(section, option):
                            self.config.remove_option(section, option)
                            self.__writeChangies()

    def add(self, section: str = "DEFAULT", option: str = None, value: any = None):
        """
        
        """
        if not option == None:
            if type(section) == str:
                if type(option) == str:
                    if(type(value) == str):
                        self.__addOption(section, option, value)
    
    def __addOption(self, section: str, option: str, value: str):
        """
        
        """
        if not section == "DEFAULT":
            if not self.config.has_section(section):
                self.config.add_section(section)
        self.config.set(section, option, value)
        self.__writeChangies()
    
    def get(self, section: str = "DEFAULT", option: str = None):
        """
        
        """
        if not option == None:
            if (self.config.has_section(section)) or (section == "DEFAULT"):
                if self.config.has_option(section, option):
                    return self.config.get(section, option)
                    

    def remove(self) -> None:
        """
        
        """
        self.__writeChangies()