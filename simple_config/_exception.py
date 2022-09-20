class configError(Exception):
    """General exception class"""

class incorrectFileNameError(configError):
    """Incorrect extension configurated file error"""
    
    def __init__(self, FileName: str) -> None:
        self.FileName = FileName
        super().__init__(FileName)

    def __str__(self) -> str:
        return f'{self.FileName} - Incorrect extension configurated file. Example: "config.ini"'

class incorrectPathError(configError):
    """Incorrect path configurated file error"""
    def __init__(self, Path) -> None:
        self.Path = Path if Path else "Unknown error"
        configError().__init__(Path)
    
    def __str__(self) -> str:
        return f'{self.Path} - Incorrect path configurated file. Example: "./settings/config"'

class configTypeError(configError):
    """Type error"""
    def __init__(self, *args) -> None:
        """
            >>> args[0] - using type
            >>> args[1] - expected type
        """
        self.UType = args[0] if args else "Unknown using Type"
        self.Type = args[1] if args else "Unknown Type"
        configError().__init__(args)
    
    def __str__(self) -> str:
        return f'Incorrect type. {type(self.UType)} is not {self.Type}"'

class notFound(configError):
    """Error called when the specified element is not found"""
    def __init__(self, *args) -> None:
        """args: 0 - searching element 1 - element type"""
        self.element = args[0] if args else "Unknown element"
        self.type = args[1] if args else "Unknown type"
        configError().__init__(args)
    
    def __str__(self) -> str:
        return f'Incorrect {self.type}. {self.element} is not found"'
