from _typeshed import Incomplete
from gunicorn import util as util

PLATFORM: Incomplete
IS_CYGWIN: Incomplete

class WorkerTmp:
    spinner: int
    def __init__(self, cfg) -> None: ...
    def notify(self) -> None: ...
    def last_update(self): ...
    def fileno(self): ...
    def close(self): ...