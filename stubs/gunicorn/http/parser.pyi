from _typeshed import Incomplete
from gunicorn.http.message import Request as Request
from gunicorn.http.unreader import IterUnreader as IterUnreader, SocketUnreader as SocketUnreader

class Parser:
    mesg_class: Incomplete
    cfg: Incomplete
    unreader: Incomplete
    mesg: Incomplete
    source_addr: Incomplete
    req_count: int
    def __init__(self, cfg, source, source_addr) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next: Incomplete

class RequestParser(Parser):
    mesg_class: Incomplete
