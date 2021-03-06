from _typeshed import Incomplete
from collections.abc import Generator
from gunicorn.http.errors import ChunkMissingTerminator as ChunkMissingTerminator, InvalidChunkSize as InvalidChunkSize, NoMoreData as NoMoreData

class ChunkedReader:
    req: Incomplete
    parser: Incomplete
    buf: Incomplete
    def __init__(self, req, unreader) -> None: ...
    def read(self, size): ...
    def parse_trailers(self, unreader, data): ...
    def parse_chunked(self, unreader) -> Generator[Incomplete, None, None]: ...
    def parse_chunk_size(self, unreader, data: Incomplete | None = ...): ...
    def get_data(self, unreader, buf) -> None: ...

class LengthReader:
    unreader: Incomplete
    length: Incomplete
    def __init__(self, unreader, length) -> None: ...
    def read(self, size): ...

class EOFReader:
    unreader: Incomplete
    buf: Incomplete
    finished: bool
    def __init__(self, unreader) -> None: ...
    def read(self, size): ...

class Body:
    reader: Incomplete
    buf: Incomplete
    def __init__(self, reader) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next: Incomplete
    def getsize(self, size): ...
    def read(self, size: Incomplete | None = ...): ...
    def readline(self, size: Incomplete | None = ...): ...
    def readlines(self, size: Incomplete | None = ...): ...
