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

Available methods:
==================

- add(section: str, option: str, value: str)
- get(section: str, option: str, gettingtype: str)
- delete(section: str, option: str)
- fullpath()
- has_option(section: str, option: str)
- has_section(section: str)

EXAMPLES:
=========


The "add" method creates a new section if it does not exist. And a new option if it doesn't exist. Otherwise, it overwrites this option
```python
config.add(section = "your_section", option = "your_option", value = "your_value") 
```
Value can be only str, int, float or complex types

The "get" method gets the desired option, if it exists. Otherwise, the error "simple_config.NotFound - Incorrect section/option" will be returned. Your_section/option is not found". The gettingtype argument can be only ["str", "int", "float", "complex"]
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

The "has_option" method returns **True** of **False** if seaching option is founded
```python
your_option = config.has_option(section = "your_section", option = "your_option")
```

The "has_section" method returns **True** of **False** if seaching section is founded
```python
your_section = config.has_section(section = "your_section")
```

About author:
=============
Author: **P3R3TS**
Email: **b.zabortsev@gmail.com**
