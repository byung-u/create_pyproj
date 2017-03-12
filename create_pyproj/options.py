"""create_pyproj create python project template command line tool."""
from datetime import datetime


class Options:
    """Options collected from input options."""
    def __init__(self) -> None:
        self.path = None  # type: str
        self.proj = None  # type: str
        self.auth = ""  # type: str

        now = datetime.now()
        self.year = now.year  # type: int
