from _typeshed import Incomplete
from gunicorn import util as util

SYSLOG_FACILITIES: Incomplete
CONFIG_DEFAULTS: Incomplete

def loggers(): ...

class SafeAtoms(dict):
    def __init__(self, atoms) -> None: ...
    def __getitem__(self, k): ...

def parse_syslog_address(addr): ...

class Logger:
    LOG_LEVELS: Incomplete
    loglevel: Incomplete
    error_fmt: str
    datefmt: str
    access_fmt: str
    syslog_fmt: str
    atoms_wrapper_class: Incomplete
    error_log: Incomplete
    access_log: Incomplete
    error_handlers: Incomplete
    access_handlers: Incomplete
    logfile: Incomplete
    lock: Incomplete
    cfg: Incomplete
    def __init__(self, cfg) -> None: ...
    def setup(self, cfg) -> None: ...
    def critical(self, msg, *args, **kwargs) -> None: ...
    def error(self, msg, *args, **kwargs) -> None: ...
    def warning(self, msg, *args, **kwargs) -> None: ...
    def info(self, msg, *args, **kwargs) -> None: ...
    def debug(self, msg, *args, **kwargs) -> None: ...
    def exception(self, msg, *args, **kwargs) -> None: ...
    def log(self, lvl, msg, *args, **kwargs) -> None: ...
    def atoms(self, resp, req, environ, request_time): ...
    def access(self, resp, req, environ, request_time) -> None: ...
    def now(self): ...
    def reopen_files(self) -> None: ...
    def close_on_exec(self) -> None: ...
