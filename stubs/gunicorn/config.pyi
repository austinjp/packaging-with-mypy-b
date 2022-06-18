from _typeshed import Incomplete
from gunicorn import util as util
from gunicorn.errors import ConfigError as ConfigError
from gunicorn.reloader import reloader_engines as reloader_engines

KNOWN_SETTINGS: Incomplete
PLATFORM: Incomplete

def make_settings(ignore: Incomplete | None = ...): ...
def auto_int(_, x): ...

class Config:
    settings: Incomplete
    usage: Incomplete
    prog: Incomplete
    env_orig: Incomplete
    def __init__(self, usage: Incomplete | None = ..., prog: Incomplete | None = ...) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    def set(self, name, value) -> None: ...
    def get_cmd_args_from_env(self): ...
    def parser(self): ...
    @property
    def worker_class_str(self): ...
    @property
    def worker_class(self): ...
    @property
    def address(self): ...
    @property
    def uid(self): ...
    @property
    def gid(self): ...
    @property
    def proc_name(self): ...
    @property
    def logger_class(self): ...
    @property
    def is_ssl(self): ...
    @property
    def ssl_options(self): ...
    @property
    def env(self): ...
    @property
    def sendfile(self): ...
    @property
    def reuse_port(self): ...
    @property
    def paste_global_conf(self): ...

class SettingMeta(type):
    def __new__(cls, name, bases, attrs): ...
    def fmt_desc(cls, desc) -> None: ...

class Setting:
    name: Incomplete
    value: Incomplete
    section: Incomplete
    cli: Incomplete
    validator: Incomplete
    type: Incomplete
    meta: Incomplete
    action: Incomplete
    default: Incomplete
    short: Incomplete
    desc: Incomplete
    nargs: Incomplete
    const: Incomplete
    def __init__(self) -> None: ...
    def add_option(self, parser) -> None: ...
    def copy(self): ...
    def get(self): ...
    def set(self, val) -> None: ...
    def __lt__(self, other): ...
    __cmp__: Incomplete

def validate_bool(val): ...
def validate_dict(val): ...
def validate_pos_int(val): ...
def validate_ssl_version(val): ...
def validate_string(val): ...
def validate_file_exists(val): ...
def validate_list_string(val): ...
def validate_list_of_existing_files(val): ...
def validate_string_to_list(val): ...
def validate_class(val): ...
def validate_callable(arity): ...
def validate_user(val): ...
def validate_group(val): ...
def validate_post_request(val): ...
def validate_chdir(val): ...
def validate_hostport(val): ...
def validate_reload_engine(val): ...
def get_default_config_file(): ...

class ConfigFile(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: str
    desc: str

class WSGIApp(Setting):
    name: str
    section: str
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class Bind(Setting):
    name: str
    action: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class Backlog(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class Workers(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: Incomplete
    desc: str

class WorkerClass(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: str
    desc: str

class WorkerThreads(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class WorkerConnections(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class MaxRequests(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class MaxRequestsJitter(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class Timeout(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class GracefulTimeout(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class Keepalive(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class LimitRequestLine(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class LimitRequestFields(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class LimitRequestFieldSize(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class Reload(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class ReloadEngine(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: str
    desc: str

class ReloadExtraFiles(Setting):
    name: str
    action: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class Spew(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class ConfigCheck(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class PrintConfig(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class PreloadApp(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class Sendfile(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    const: bool
    desc: str

class ReusePort(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class Chdir(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    default: Incomplete
    desc: str

class Daemon(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class Env(Setting):
    name: str
    action: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class Pidfile(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class WorkerTmpDir(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class User(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class Group(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class Umask(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    type: Incomplete
    default: int
    desc: str

class Initgroups(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class TmpUploadDir(Setting):
    name: str
    section: str
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class SecureSchemeHeader(Setting):
    name: str
    section: str
    validator: Incomplete
    default: Incomplete
    desc: str

class ForwardedAllowIPS(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class AccessLog(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class DisableRedirectAccessToSyslog(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class AccessLogFormat(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: str
    desc: str

class ErrorLog(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: str
    desc: str

class Loglevel(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: str
    desc: str

class CaptureOutput(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class LoggerClass(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: str
    desc: str

class LogConfig(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class LogConfigDict(Setting):
    name: str
    section: str
    validator: Incomplete
    default: Incomplete
    desc: str

class SyslogTo(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: str
    desc: str

class Syslog(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class SyslogPrefix(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class SyslogFacility(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: str
    desc: str

class EnableStdioInheritance(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    default: bool
    action: str
    desc: str

class StatsdHost(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    default: Incomplete
    validator: Incomplete
    desc: str

class DogstatsdTags(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    default: str
    validator: Incomplete
    desc: str

class StatsdPrefix(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    default: str
    validator: Incomplete
    desc: str

class Procname(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class DefaultProcName(Setting):
    name: str
    section: str
    validator: Incomplete
    default: str
    desc: str

class PythonPath(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class Paste(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class OnStarting(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def on_starting(server) -> None: ...
    default: Incomplete
    desc: str

class OnReload(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def on_reload(server) -> None: ...
    default: Incomplete
    desc: str

class WhenReady(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def when_ready(server) -> None: ...
    default: Incomplete
    desc: str

class Prefork(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def pre_fork(server, worker) -> None: ...
    default: Incomplete
    desc: str

class Postfork(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def post_fork(server, worker) -> None: ...
    default: Incomplete
    desc: str

class PostWorkerInit(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def post_worker_init(worker) -> None: ...
    default: Incomplete
    desc: str

class WorkerInt(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def worker_int(worker) -> None: ...
    default: Incomplete
    desc: str

class WorkerAbort(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def worker_abort(worker) -> None: ...
    default: Incomplete
    desc: str

class PreExec(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def pre_exec(server) -> None: ...
    default: Incomplete
    desc: str

class PreRequest(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def pre_request(worker, req) -> None: ...
    default: Incomplete
    desc: str

class PostRequest(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def post_request(worker, req, environ, resp) -> None: ...
    default: Incomplete
    desc: str

class ChildExit(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def child_exit(server, worker) -> None: ...
    default: Incomplete
    desc: str

class WorkerExit(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def worker_exit(server, worker) -> None: ...
    default: Incomplete
    desc: str

class NumWorkersChanged(Setting):
    name: str
    section: str
    validator: Incomplete
    type: Incomplete
    def nworkers_changed(server, new_value, old_value) -> None: ...
    default: Incomplete
    desc: str

class OnExit(Setting):
    name: str
    section: str
    validator: Incomplete
    def on_exit(server) -> None: ...
    default: Incomplete
    desc: str

class ProxyProtocol(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    default: bool
    action: str
    desc: str

class ProxyAllowFrom(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    default: str
    desc: str

class KeyFile(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class CertFile(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class SSLVersion(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    default: Incomplete
    desc: str

class CertReqs(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    default: Incomplete
    desc: str

class CACerts(Setting):
    name: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class SuppressRaggedEOFs(Setting):
    name: str
    section: str
    cli: Incomplete
    action: str
    default: bool
    validator: Incomplete
    desc: str

class DoHandshakeOnConnect(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str

class Ciphers(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    default: Incomplete
    desc: str

class PasteGlobalConf(Setting):
    name: str
    action: str
    section: str
    cli: Incomplete
    meta: str
    validator: Incomplete
    default: Incomplete
    desc: str

class StripHeaderSpaces(Setting):
    name: str
    section: str
    cli: Incomplete
    validator: Incomplete
    action: str
    default: bool
    desc: str
