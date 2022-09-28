Description
===========

The simple_config package is used to simplify working with configuration files.

To use the package, you must:
=============================

Adding a package to your project
```python
from simple_config import config
```

Creating configurating file
```python
path = "./your_config_path"
filename = "your_filename.ini"

# Default path = "./", filename = "config.ini"
config = config(path = path, filename = filename)
``` 

The "add" method creates a new section if it does not exist. And a new option if it doesn't exist. Otherwise, it overwrites this option 
```python
config.add(section = "your_section", option = "your_option", value = "your_value") 
```

The "get" method gets the desired option, if it exists. Otherwise, the error "simple_config.NotFound - Incorrect section/option" will be returned. Your_section/option is not found". The gettingtype argument can be ["str", "int", "float", "complex"]
```python
config.get(section = "your_section", option = "your_option", gettingtype = "str")
```

The "delete" method deletes the desired option, if it exists. If the option was the only one in the current section, the section is also deleted. Otherwise, the method leads to an error.
```python
config.delete(section = "your_section", option = "your_option")
```

The "fullpath" method returns the full path to the configuration file. "your_config_path/your_filename.ini"
```python
fullpath = config.fullpath()
```

About author:
=============
Author: P3R3TS
