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
        handle_whitespace=lambda read, stream, x: None,

        is_macro=lambda x: False,
        handle_macro_character=lambda read, stream, x: None,

        is_constituent=lambda x: False,
        handle_constituent=lambda read, stream, x: None,

        is_valid=lambda x: False,
        signal=lambda s: s,
    )
    result = read.read_dispatch(n, None, None, "")
    assert result == "reader-error"

def test_read_dispatch_whitespace_character():
    n = SimpleNamespace(
        is_whitespace=lambda x: True,
        handle_whitespace=lambda read, stream, x: "handle-whitespace",

        is_macro=lambda x: False,
        handle_macro_character=lambda read, stream, x: "handle-macro",

        is_constituent=lambda x: False,
        handle_constituent=lambda read, stream, x: "handle-constituent",

        is_valid=lambda x: False,
        signal=lambda s: s,
    )
    result = read.read_dispatch(n, None, None, "")
    assert result == "handle-whitespace"

def test_read_dispatch_macro_character():
    n = SimpleNamespace(
        is_whitespace=lambda x: False,
        handle_whitespace=lambda read, stream, x: "handle-whitespace",

        is_macro=lambda x: True,
        handle_macro_character=lambda read, stream, x: "handle-macro",

        is_constituent=lambda x: False,
        handle_constituent=lambda read, stream, x: "handle-constituent",

        is_valid=lambda x: False,
        signal=lambda s: s,
    )
    result = read.read_dispatch(n, None, None, "")
    assert result == "handle-macro"

def run_tests():
    test_read_end_of_file()
    test_read_dispatch_invalid_character()
    test_read_dispatch_whitespace_character()
    test_read_dispatch_macro_character()

    print("test_read : passed")
