import read
import streams
from types import SimpleNamespace

def set_fields(d, fields):
    for k, v in fields.items():
        d[k] = v

def set_return(state, value):
    state["return"] = value
    state["signal"] = None

def set_signal(state, value):
    state["return"] = None
    state["signal"] = value

def fake_read_token_dispatch(state, current, stream, y):
    current["token"] += y
    if current["status"] == "even":
        current["status"] = "odd"
        return
    else:
        return current["token"]

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
        read_token=lambda state, initial_status, stream, x: x + "BC"
    )
    state = {}
    result = read.handle_constituent(n, state, None, None, "A")
    assert result == "ABC"

def test_read_token():
    n = SimpleNamespace(
        read_token_dispatch=fake_read_token_dispatch,
    )
    state = {
        "signal": None
    }
    stream = streams.create("BC")
    result = read.read_token(n, state, "even", stream, "A")
    result == "ABC"

def test_read_end_of_file():
    n = SimpleNamespace(
        handle_end_of_file=lambda: "eof",
        read_dispatch=None,
    )
    state = {
        "return": None,
        "signal": None,
        "status": "read",
    }
    stream = streams.create("")
    result = read.read(n, state, stream)
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
