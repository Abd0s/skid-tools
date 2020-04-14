from .exceptions import MissingConfigFile
import sys

try:
    import config
except ModuleNotFoundError:
    raise MissingConfigFile("No config.py file found, use --init to initilize one.")

