import io
import pytest
from enum import Enum
from pathlib import Path
from lib.util import ErrorT
from tf_plan_view import (
    parse_args
)

DATA = Path(__file__).parent / "data"

def load_text_data(file_name: str) -> str:
    return (DATA / file_name).read_text()

def load_binary_data(file_name: str) -> bytes:
    return (DATA / file_name).read_bytes()

# TESTS
def test_stub() -> None:
    assert True
