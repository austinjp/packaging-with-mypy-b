from _typeshed import Incomplete
from gunicorn import debug as debug, util as util
from gunicorn.arbiter import Arbiter as Arbiter
from gunicorn.config import Config as Config, get_default_config_file as get_default_config_file

class BaseApplication:
    usage: Incomplete
    cfg: Incomplete
    callable: Incomplete
    prog: Incomplete
    logger: Incomplete
    def __init__(self, usage: Incomplete | None = ..., prog: Incomplete | None = ...) -> None: ...
    def do_load_config(self) -> None: ...
    def load_default_config(self) -> None: ...
    def init(self, parser, opts, args) -> None: ...
    def load(self) -> None: ...
    def load_config(self) -> None: ...
    def reload(self) -> None: ...
    def wsgi(self): ...
    def run(self) -> None: ...

class Application(BaseApplication):
    def chdir(self) -> None: ...
    def get_config_from_filename(self, filename): ...
    def get_config_from_module_name(self, module_name): ...
    def load_config_from_module_name_or_filename(self, location): ...
    def load_config_from_file(self, filename): ...
    def load_config(self) -> None: ...
    def run(self) -> None: ...