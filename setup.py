from setuptools import setup, find_packages
from os.path import join, dirname

import src

setup(
    name = "simple_config",
    version = src.__version__,
    packages = find_packages(),
    long_description = open(join(dirname(__file__), "README.md")).read(),
    install_requires = open(join(dirname(__file__), "requirements.txt")).read(),
    license = open(join(dirname(__file__), "LICENSE")).read(),
)