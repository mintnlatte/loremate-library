from src.parser import _fib
from src.utils import format_output


def test_fib_basic():
    assert _fib(10) == 55


def test_format_list():
    assert format_output([1, 1, 2]) == "1, 1, 2"
