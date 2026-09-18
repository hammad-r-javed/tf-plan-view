import sys
from enum import Enum
from typing import Any, TextIO, TypeVar
from dataclasses import dataclass

@dataclass
class ErrorT:
    value: str

class LogT(Enum):
    INF = ""
    OK = "\033[0;32m"
    DBG = '\033[2;30m'
    CMD = "\033[0;34m"
    WRN = "\033[0;33m"
    ERR = "\033[0;31m"

def log(log_type: LogT, text: str) -> None:
    stream: TextIO = sys.stderr if log_type in (LogT.WRN, LogT.ERR) else sys.stdout
    print(f"{log_type.value}{text}\033[0m", file=stream)

T = TypeVar("T")
def require(res: T | ErrorT, error_msg: str) -> T:
    if isinstance(res, ErrorT):
        log(LogT.ERR, f"{error_msg}: {res.value}")
        sys.exit(1)
    return res
