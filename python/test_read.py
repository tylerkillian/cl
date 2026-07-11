import read
import streams
from types import SimpleNamespace

def set_return(state, value):
    state["return"] = value
    state["signal"] = None

def set_signal(state, value):
    state["return"] = None
    state["signal"] = value

def test_read_dispatch_invalid_character():
    n = SimpleNamespace(
        is_whitespace=lambda x: False,
        handle_whitespace=lambda state, read, stream, x: set_return(state, "handle-whitespace"),

        is_macro=lambda x: False,
        handle_macro_character=lambda state, read, stream, x: set_return(state, "handle-macro"),

        is_single_escape=lambda x: False,
        handle_single_escape=lambda state, read, stream, x: set_return(state, "handle-single-escape"),

        is_multiple_escape=lambda x: False,
        handle_multiple_escape=lambda state, read, stream, x: set_return(state, "handle-multiple-escape"),

        is_constituent=lambda x: False,
        handle_constituent=lambda state, read, stream, x: set_return(state, "handle-constituent"),

        is_valid=lambda x: False,
        signal=lambda state, s: set_signal(state, s),
    )
    state = {
        "return": None,
        "signal": None
    }
    read.read_dispatch(n, state, None, None, "")
    assert state["return"] == None
    assert state["signal"] == "reader-error"

def test_read_dispatch_whitespace_character():
    n = SimpleNamespace(
        is_whitespace=lambda x: True,
        handle_whitespace=lambda state, read, stream, x: set_return(state, "handle-whitespace"),

        is_macro=lambda x: False,
        handle_macro_character=lambda state, read, stream, x: set_return(state, "handle-macro"),

        is_single_escape=lambda x: False,
        handle_single_escape=lambda state, read, stream, x: set_return(state, "handle-single-escape"),

        is_multiple_escape=lambda x: False,
        handle_multiple_escape=lambda state, read, stream, x: set_return(state, "handle-multiple-escape"),

        is_constituent=lambda x: False,
        handle_constituent=lambda state, read, stream, x: set_return(state, "handle-constituent"),

        is_valid=lambda x: False,
        signal=lambda state, s: set_signal(state, s),
    )
    state = {}
    result = read.read_dispatch(n, state, None, None, "")
    assert state["return"] == "handle-whitespace"
    assert state["signal"] == None

def test_read_dispatch_macro_character():
    n = SimpleNamespace(
        is_whitespace=lambda x: False,
        handle_whitespace=lambda state, read, stream, x: set_return(state, "handle-whitespace"),

        is_macro=lambda x: True,
        handle_macro_character=lambda state, read, stream, x: set_return(state, "handle-macro"),

        is_single_escape=lambda x: False,
        handle_single_escape=lambda state, read, stream, x: set_return(state, "handle-single-escape"),

        is_multiple_escape=lambda x: False,
        handle_multiple_escape=lambda state, read, stream, x: set_return(state, "handle-multiple-escape"),

        is_constituent=lambda x: False,
        handle_constituent=lambda state, read, stream, x: set_return(state, "handle-constituent"),

        is_valid=lambda x: False,
        signal=lambda state, s: set_signal(state, s),
    )
    state = {}
    result = read.read_dispatch(n, state, None, None, "")
    assert state["return"] == "handle-macro"
    assert state["signal"] == None

def test_read_dispatch_single_escape_character():
    n = SimpleNamespace(
        is_whitespace=lambda x: False,
        handle_whitespace=lambda state, read, stream, x: set_return(state, "handle-whitespace"),

        is_macro=lambda x: False,
        handle_macro_character=lambda state, read, stream, x: set_return(state, "handle-macro"),

        is_single_escape=lambda x: True,
        handle_single_escape=lambda state, read, stream, x: set_return(state, "handle-single-escape"),

        is_multiple_escape=lambda x: False,
        handle_multiple_escape=lambda state, read, stream, x: set_return(state, "handle-multiple-escape"),

        is_constituent=lambda x: False,
        handle_constituent=lambda state, read, stream, x: set_return(state, "handle-constituent"),

        is_valid=lambda x: False,
        signal=lambda state, s: set_signal(state, s),
    )
    state = {}
    result = read.read_dispatch(n, state, None, None, "")
    assert state["return"] == "handle-single-escape"
    assert state["signal"] == None

def test_read_dispatch_multiple_escape_character():
    n = SimpleNamespace(
        is_whitespace=lambda x: False,
        handle_whitespace=lambda state, read, stream, x: set_return(state, "handle-whitespace"),

        is_macro=lambda x: False,
        handle_macro_character=lambda state, read, stream, x: set_return(state, "handle-macro"),

        is_single_escape=lambda x: False,
        handle_single_escape=lambda state, read, stream, x: set_return(state, "handle-single-escape"),

        is_multiple_escape=lambda x: True,
        handle_multiple_escape=lambda state, read, stream, x: set_return(state, "handle-multiple-escape"),

        is_constituent=lambda x: False,
        handle_constituent=lambda state, read, stream, x: set_return(state, "handle-constituent"),

        is_valid=lambda x: False,
        signal=lambda state, s: set_signal(state, s),
    )
    state = {}
    result = read.read_dispatch(n, state, None, None, "")
    assert state["return"] == "handle-multiple-escape"
    assert state["signal"] == None

def test_read_dispatch_constituent_character():
    n = SimpleNamespace(
        is_whitespace=lambda x: False,
        handle_whitespace=lambda state, read, stream, x: set_return(state, "handle-whitespace"),

        is_macro=lambda x: False,
        handle_macro_character=lambda state, read, stream, x: set_return(state, "handle-macro"),

        is_single_escape=lambda x: False,
        handle_single_escape=lambda state, read, stream, x: set_return(state, "handle-single-escape"),

        is_multiple_escape=lambda x: False,
        handle_multiple_escape=lambda state, read, stream, x: set_return(state, "handle-multiple-escape"),

        is_constituent=lambda x: True,
        handle_constituent=lambda state, read, stream, x: set_return(state, "handle-constituent"),

        is_valid=lambda x: False,
        signal=lambda state, s: set_signal(state, s),
    )
    state = {}
    result = read.read_dispatch(n, state, None, None, "")
    assert state["return"] == "handle-constituent"
    assert state["signal"] == None

def test_handle_constituent():
    n = SimpleNamespace(
        read_token=lambda cl_state, read_token_state, stream: set_return(cl_state, read_token_state["token"]),
    )
    state = {}
    result = read.handle_constituent(n, state, None, None, "A")
    assert state["return"] == "A"
    assert state["signal"] == None

def test_read_token():
    print("IMPLEMENT TESTS FOR read_token()")

def test_read_end_of_file():
    n = SimpleNamespace(
        handle_end_of_file=lambda: "eof",
        read_dispatch=None,
    )
    stream = streams.create("")
    result = read.read(n, stream)
    assert result == "eof"

def run_tests():
    test_read_dispatch_invalid_character()
    test_read_dispatch_whitespace_character()
    test_read_dispatch_macro_character()
    test_read_dispatch_single_escape_character()
    test_read_dispatch_multiple_escape_character()
    test_read_dispatch_constituent_character()

    test_handle_constituent()

    test_read_token()

    test_read_end_of_file()

    print("test_read : passed")
