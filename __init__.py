import atexit as _atexit

from ._config import config as _config

__version__ = "0.0.1"

__all__ = ["config"]

config = _config(
    path = False,
    filename = "config.ini"
)

_atexit.register(config.remove)