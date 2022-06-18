from _typeshed import Incomplete
from gunicorn.http.body import Body as Body, ChunkedReader as ChunkedReader, EOFReader as EOFReader, LengthReader as LengthReader
from gunicorn.http.errors import ForbiddenProxyRequest as ForbiddenProxyRequest, InvalidHTTPVersion as InvalidHTTPVersion, InvalidHeader as InvalidHeader, InvalidHeaderName as InvalidHeaderName, InvalidProxyLine as InvalidProxyLine, InvalidRequestLine as InvalidRequestLine, InvalidRequestMethod as InvalidRequestMethod, InvalidSchemeHeaders as InvalidSchemeHeaders, LimitRequestHeaders as LimitRequestHeaders, LimitRequestLine as LimitRequestLine, NoMoreData as NoMoreData
from gunicorn.util import bytes_to_str as bytes_to_str, split_request_uri as split_request_uri

MAX_REQUEST_LINE: int
MAX_HEADERS: int
DEFAULT_MAX_HEADERFIELD_SIZE: int
HEADER_RE: Incomplete
METH_RE: Incomplete
VERSION_RE: Incomplete

class Message:
    cfg: Incomplete
    unreader: Incomplete
    peer_addr: Incomplete
    version: Incomplete
    headers: Incomplete
    trailers: Incomplete
    body: Incomplete
    scheme: Incomplete
    limit_request_fields: Incomplete
    limit_request_field_size: Incomplete
    max_buffer_headers: Incomplete
    def __init__(self, cfg, unreader, peer_addr) -> None: ...
    def parse(self, unreader) -> None: ...
    def parse_headers(self, data): ...
    def set_body_reader(self) -> None: ...
    def should_close(self): ...

class Request(Message):
    method: Incomplete
    uri: Incomplete
    path: Incomplete
    query: Incomplete
    fragment: Incomplete
    limit_request_line: Incomplete
    req_number: Incomplete
    proxy_protocol_info: Incomplete
    def __init__(self, cfg, unreader, peer_addr, req_number: int = ...) -> None: ...
    def get_data(self, unreader, buf, stop: bool = ...) -> None: ...
    headers: Incomplete
    def parse(self, unreader): ...
    def read_line(self, unreader, buf, limit: int = ...): ...
    def proxy_protocol(self, line): ...
    def proxy_protocol_access_check(self) -> None: ...
    def parse_proxy_protocol(self, line) -> None: ...
    version: Incomplete
    def parse_request_line(self, line_bytes) -> None: ...
    body: Incomplete
    def set_body_reader(self) -> None: ...
