import threading
from _typeshed import Incomplete

COMPILED_EXT_RE: Incomplete

class Reloader(threading.Thread):
    def __init__(self, extra_files: Incomplete | None = ..., interval: int = ..., callback: Incomplete | None = ...) -> None: ...
    def add_extra_file(self, filename) -> None: ...
    def get_files(self): ...
    def run(self) -> None: ...

has_inotify: bool

class InotifyReloader(threading.Thread):
    event_mask: Incomplete
    def __init__(self, extra_files: Incomplete | None = ..., callback: Incomplete | None = ...) -> None: ...
    def add_extra_file(self, filename) -> None: ...
    def get_dirs(self): ...
    def run(self) -> None: ...

class InotifyReloader:
    def __init__(self, callback: Incomplete | None = ...) -> None: ...

preferred_reloader: Incomplete
reloader_engines: Incomplete
