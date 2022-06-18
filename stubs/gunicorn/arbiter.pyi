from _typeshed import Incomplete
from gunicorn import SERVER_SOFTWARE as SERVER_SOFTWARE, sock as sock, systemd as systemd, util as util
from gunicorn.errors import AppImportError as AppImportError, HaltServer as HaltServer
from gunicorn.pidfile import Pidfile as Pidfile

class Arbiter:
    WORKER_BOOT_ERROR: int
    APP_LOAD_ERROR: int
    START_CTX: Incomplete
    LISTENERS: Incomplete
    WORKERS: Incomplete
    PIPE: Incomplete
    SIG_QUEUE: Incomplete
    SIGNALS: Incomplete
    SIG_NAMES: Incomplete
    log: Incomplete
    pidfile: Incomplete
    systemd: bool
    worker_age: int
    reexec_pid: int
    master_pid: int
    master_name: str
    def __init__(self, app) -> None: ...
    num_workers: Incomplete
    app: Incomplete
    cfg: Incomplete
    worker_class: Incomplete
    address: Incomplete
    timeout: Incomplete
    proc_name: Incomplete
    def setup(self, app): ...
    pid: Incomplete
    def start(self) -> None: ...
    def init_signals(self) -> None: ...
    def signal(self, sig, frame) -> None: ...
    def run(self) -> None: ...
    def handle_chld(self, sig, frame) -> None: ...
    def handle_hup(self) -> None: ...
    def handle_term(self) -> None: ...
    def handle_int(self) -> None: ...
    def handle_quit(self) -> None: ...
    def handle_ttin(self) -> None: ...
    def handle_ttou(self) -> None: ...
    def handle_usr1(self) -> None: ...
    def handle_usr2(self) -> None: ...
    def handle_winch(self) -> None: ...
    def maybe_promote_master(self) -> None: ...
    def wakeup(self) -> None: ...
    def halt(self, reason: Incomplete | None = ..., exit_status: int = ...) -> None: ...
    def sleep(self) -> None: ...
    def stop(self, graceful: bool = ...) -> None: ...
    def reexec(self) -> None: ...
    def reload(self) -> None: ...
    def murder_workers(self) -> None: ...
    def reap_workers(self) -> None: ...
    def manage_workers(self): ...
    def spawn_worker(self): ...
    def spawn_workers(self) -> None: ...
    def kill_workers(self, sig) -> None: ...
    def kill_worker(self, pid, sig) -> None: ...
