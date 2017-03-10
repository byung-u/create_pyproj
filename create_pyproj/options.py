"""create_pyproj create python project template command line tool."""
import configparser
from create_pyproj import defaults


class Options:
    """Options collected from input options."""
    def __init__(self) -> None:
        self.path = None  # type: str
        self.proj = None  # type: str
