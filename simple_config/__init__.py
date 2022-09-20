from ._config import config as _Config
from ._exception import configError as _Error

__version__ = "0.0.1"

__all__ = ["config"]

Error = _Error

config = _Config