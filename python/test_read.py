import read
import streams
from types import SimpleNamespace

def test_read_end_of_file():
    n = SimpleNamespace(
        handle_end_of_file=lambda: "eof",
        read_dispatch=None,
    )
    stream = streams.create("")
    result = read.read(n, stream)
    assert result == "eof"

def test_read_dispatch_invalid_character():
    n = SimpleNamespace(
        is_whitespace=lambda x: False,
        is_macro=lambda x: False,
        is_constituent=lambda x: False,
        is_valid=lambda x: False,
        signal=lambda s: s,
    )
    result = read.read_dispatch(n, None, None, "")
    assert result == "reader-error"

def run_tests():
    test_read_end_of_file()
    test_read_dispatch_invalid_character()

    print("test_read : passed")
