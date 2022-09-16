import atexit as _atexit

from ._config import config as _config
from _exception import configError as _Error

__version__ = "0.0.1"

__all__ = ["config"]

Error = _Error

config = _config(
    path = None,
    filename = "config.ini"
)

_atexit.register(config.remove)