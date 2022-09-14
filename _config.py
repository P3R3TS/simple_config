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
        print ("create configuration file")
    
    def fullpath(self) -> None:
        fullpath = f"{self.path}/{self.filename}"
        return fullpath

    def add(section: str = None, settings: str = None):
        pass

    def remove(self) -> None:
        """
        
        """
        pass

conf1 = config( 
    path = "./conf",
    filename = "Settings.ini"
    )
print(conf1.fullpath())

