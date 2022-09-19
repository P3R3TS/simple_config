from pathlib import Path


def fullpath(path: str = "configs", filename: str = "config.ini") -> str:
    filename: Path = Path(filename)
    path: Path = Path(path)
    return path / filename

print (fullpath())

print (fullpath(".//.//crup//", "configs."))