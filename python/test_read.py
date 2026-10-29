import read
import streams
from types import SimpleNamespace

def set_fields(d, fields):
    for k, v in fields.items():
        d[k] = v

def set_signal(state, value):
    state["signal"] = value

def fake_read_token_dispatch(state, current, stream, y):
    current["token"] += y
    if current["status"] == "even":
        current["status"] = "odd"
        return None
    else:
        return current["token"]

def create_fake_read_dispatch(save_inputs):
    def result(state, read, stream, x):
        assert len(x) == 1
        save_inputs.append(x)
        if x == "R":
            return "".join(save_inputs)
        elif x == "S":
            state["signal"] = "fake-signal"
            return None
        else:
            return None
    return result

def test_read_dispatch_invalid_character():
    n = SimpleNamespace(
        is_whitespace_character=lambda x: False,
        read_dispatch_handle_whitespace_character=lambda state, read, stream, x: "handle-whitespace",

        is_macro=lambda x: False,
        read_dispatch_handle_macro_character=lambda state, read, stream, x: "handle-macro",

        is_single_escape=lambda x: False,
        read_dispatch_handle_single_escape=lambda state, read, stream, x: "handle-single-escape",

        is_multiple_escape=lambda x: False,
        read_dispatch_handle_multiple_escape=lambda state, read, stream, x: "handle-multiple-escape",

        is_constituent=lambda x: False,
        read_dispatch_handle_constituent=lambda state, read, stream, x: "handle-constituent",

        is_valid=lambda x: False,
        signal=set_signal,
    )
    state = {
        "signal": None
    }
    result = read.read_dispatch(n, state, None, None, "")
    assert result == None
    assert state["signal"] == "reader-error"

def test_read_dispatch_whitespace_character():
    n = SimpleNamespace(
        is_whitespace_character=lambda x: True,
        read_dispatch_handle_whitespace_character=lambda state, read, stream, x: "handle-whitespace",

        is_macro=lambda x: False,
        read_dispatch_handle_macro_character=lambda state, read, stream, x: "handle-macro",

        is_single_escape=lambda x: False,
        read_dispatch_handle_single_escape=lambda state, read, stream, x: "handle-single-escape",

        is_multiple_escape=lambda x: False,
        read_dispatch_handle_multiple_escape=lambda state, read, stream, x: "handle-multiple-escape",

        is_constituent=lambda x: False,
        read_dispatch_handle_constituent=lambda state, read, stream, x: "handle-constituent",

        is_valid=lambda x: False,
        signal=set_signal,
    )
    result = read.read_dispatch(n, None, None, None, "")
    assert result == "handle-whitespace"

def test_read_dispatch_macro_character():
    n = SimpleNamespace(
        is_whitespace_character=lambda x: False,
        read_dispatch_handle_whitespace_character=lambda state, read, stream, x: "handle-whitespace",

        is_macro=lambda x: True,
        read_dispatch_handle_macro_character=lambda state, read, stream, x: "handle-macro",

        is_single_escape=lambda x: False,
        read_dispatch_handle_single_escape=lambda state, read, stream, x: "handle-single-escape",

        is_multiple_escape=lambda x: False,
        read_dispatch_handle_multiple_escape=lambda state, read, stream, x: "handle-multiple-escape",

        is_constituent=lambda x: False,
        read_dispatch_handle_constituent=lambda state, read, stream, x: "handle-constituent",

        is_valid=lambda x: False,
        signal=set_signal,
    )
    result = read.read_dispatch(n, None, None, None, "")
    assert result == "handle-macro"

def test_read_dispatch_single_escape_character():
    n = SimpleNamespace(
        is_whitespace_character=lambda x: False,
        read_dispatch_handle_whitespace_character=lambda state, read, stream, x: "handle-whitespace",

        is_macro=lambda x: False,
        read_dispatch_handle_macro_character=lambda state, read, stream, x: "handle-macro",

        is_single_escape=lambda x: True,
        read_dispatch_handle_single_escape=lambda state, read, stream, x: "handle-single-escape",

        is_multiple_escape=lambda x: False,
        read_dispatch_handle_multiple_escape=lambda state, read, stream, x: "handle-multiple-escape",

        is_constituent=lambda x: False,
        read_dispatch_handle_constituent=lambda state, read, stream, x: "handle-constituent",

        is_valid=lambda x: False,
        signal=set_signal,
    )
    result = read.read_dispatch(n, None, None, None, "")
    assert result == "handle-single-escape"

def test_read_dispatch_multiple_escape_character():
    n = SimpleNamespace(
        is_whitespace_character=lambda x: False,
        read_dispatch_handle_whitespace_character=lambda state, read, stream, x: "handle-whitespace",

        is_macro=lambda x: False,
        read_dispatch_handle_macro_character=lambda state, read, stream, x: "handle-macro",

        is_single_escape=lambda x: False,
        read_dispatch_handle_single_escape=lambda state, read, stream, x: "handle-single-escape",

        is_multiple_escape=lambda x: True,
        read_dispatch_handle_multiple_escape=lambda state, read, stream, x: "handle-multiple-escape",

        is_constituent=lambda x: False,
        read_dispatch_handle_constituent=lambda state, read, stream, x: "handle-constituent",

        is_valid=lambda x: False,
        signal=set_signal,
    )
    result = read.read_dispatch(n, None, None, None, "")
    assert result == "handle-multiple-escape"

def test_read_dispatch_constituent_character():
    n = SimpleNamespace(
        is_whitespace_character=lambda x: False,
        read_dispatch_handle_whitespace_character=lambda state, read, stream, x: "handle-whitespace",

        is_macro=lambda x: False,
        read_dispatch_handle_macro_character=lambda state, read, stream, x: "handle-macro",

        is_single_escape=lambda x: False,
        read_dispatch_handle_single_escape=lambda state, read, stream, x: "handle-single-escape",

        is_multiple_escape=lambda x: False,
        read_dispatch_handle_multiple_escape=lambda state, read, stream, x: "handle-multiple-escape",

        is_constituent=lambda x: True,
        read_dispatch_handle_constituent=lambda state, read, stream, x: "handle-constituent",

        is_valid=lambda x: False,
        signal=set_signal,
    )
    result = read.read_dispatch(n, None, None, None, "")
    assert result == "handle-constituent"

def test_read_dispatch_handle_whitespace_character():
    result = read.read_dispatch_handle_whitespace_character(None, None, None, None, None)
    assert result == None

def test_read_dispatch_handle_macro_character():
    n = SimpleNamespace(
        get_reader_macro_function=lambda read, x: (lambda stream, x: "macro-result-" + x)
    )
    result = read.read_dispatch_handle_macro_character(n, None, None, None, "|")
    assert result == "macro-result-|"

def test_read_dispatch_handle_single_escape_character():
    n = SimpleNamespace(
        signal=set_signal,
        read_token=lambda state, initial_status, stream, x: x + "BC"
    )

    state = {
        "signal": None
    }
    stream = streams.create("")
    result = read.read_dispatch_handle_single_escape_character(n, state, None, stream, "'")
    assert result == None
    assert state["signal"] == "end-of-file"

    state = {
        "signal": None
    }
    stream = streams.create("A")
    result = read.read_dispatch_handle_single_escape_character(n, state, None, stream, "'")
    assert result == "ABC"
    assert state["signal"] == None

def test_read_dispatch_handle_multiple_escape_character():
    n = SimpleNamespace(
        read_token=lambda state, initial_status, stream, x: "ABC"
    )

    result = read.read_dispatch_handle_multiple_escape_character(n, None, None, None, "|")
    assert result == "ABC"

def test_read_dispatch_handle_constituent_character():
    n = SimpleNamespace(
        read_token=lambda state, initial_status, stream, x: x + "BC"
    )
    result = read.read_dispatch_handle_constituent_character(n, None, None, None, "A")
    assert result == "ABC"

def test_read_token_even_dispatch_constituent_or_nonterminating_macro_character():
    n = SimpleNamespace(
        is_constituent_or_nonterminating_macro_character=lambda x: True,
        read_token_even_dispatch_handle_constituent_or_nonterminating_macro_character=lambda state, current, read, stream, x: "handle-constituent-or-nonterminating-macro",

        is_single_escape_character=lambda x: False,
        read_token_even_dispatch_handle_single_escape_character=lambda state, read, stream, x: "handle-single-escape",

        is_multiple_escape_character=lambda x: False,
        read_token_even_dispatch_handle_multiple_escape_character=lambda state, current, read, stream, x: "handle-multiple-escape",

        is_valid_character=lambda x: True,
        signal=set_signal,

        is_terminating_macro_character=lambda x: False,
        read_token_even_dispatch_handle_terminating_macro_character=lambda state, current, read, stream, x: "handle-terminating-macro",

        is_whitespace_character=lambda x: False,
        read_token_even_dispatch_handle_whitespace_character=lambda state, current, read, stream, x: "handle-whitespace"
    )
    result = read.read_token_even_dispatch(n, None, None, None, None, "")
    assert result == "handle-constituent-or-nonterminating-macro"

def test_read_token_even_dispatch_single_escape_character():
    n = SimpleNamespace(
        is_constituent_or_nonterminating_macro_character=lambda x: False,
        read_token_even_dispatch_handle_constituent_or_nonterminating_macro_character=lambda state, current, read, stream, x: "handle-constituent-or-nonterminating-macro",

        is_single_escape_character=lambda x: True,
        read_token_even_dispatch_handle_single_escape_character=lambda state, current, read, stream, x: "handle-single-escape",

        is_multiple_escape_character=lambda x: False,
        read_token_even_dispatch_handle_multiple_escape_character=lambda state, current, read, stream, x: "handle-multiple-escape",

        is_valid_character=lambda x: True,
        signal=set_signal,

        is_terminating_macro_character=lambda x: False,
        read_token_even_dispatch_handle_terminating_macro_character=lambda state, current, read, stream, x: "handle-terminating-macro",

        is_whitespace_character=lambda x: False,
        read_token_even_dispatch_handle_whitespace_character=lambda state, current, read, stream, x: "handle-whitespace"
    )
    result = read.read_token_even_dispatch(n, None, None, None, None, "")
    assert result == "handle-single-escape"

def test_read_token_even_dispatch_multiple_escape_character():
    n = SimpleNamespace(
        is_constituent_or_nonterminating_macro_character=lambda x: False,
        read_token_even_dispatch_handle_constituent_or_nonterminating_macro_character=lambda state, current, read, stream, x: "handle-constituent-or-nonterminating-macro",

        is_single_escape_character=lambda x: False,
        read_token_even_dispatch_handle_single_escape_character=lambda state, current, read, stream, x: "handle-single-escape",

        is_multiple_escape_character=lambda x: True,
        read_token_even_dispatch_handle_multiple_escape_character=lambda state, current, read, stream, x: "handle-multiple-escape",

        is_valid_character=lambda x: True,
        signal=set_signal,

        is_terminating_macro_character=lambda x: False,
        read_token_even_dispatch_handle_terminating_macro_character=lambda state, current, read, stream, x: "handle-terminating-macro",

        is_whitespace_character=lambda x: False,
        read_token_even_dispatch_handle_whitespace_character=lambda state, current, read, stream, x: "handle-whitespace"
    )
    result = read.read_token_even_dispatch(n, None, None, None, None, "")
    assert result == "handle-multiple-escape"

def test_read_token_even_dispatch_invalid_character():
    n = SimpleNamespace(
        is_constituent_or_nonterminating_macro_character=lambda x: False,
        read_token_even_dispatch_handle_constituent_or_nonterminating_macro_character=lambda state, current, read, stream, x: "handle-constituent-or-nonterminating-macro",

        is_single_escape_character=lambda x: False,
        read_token_even_dispatch_handle_single_escape_character=lambda state, current, read, stream, x: "handle-single-escape",

        is_multiple_escape_character=lambda x: False,
        read_token_even_dispatch_handle_multiple_escape_character=lambda state, current, read, stream, x: "handle-multiple-escape",

        is_valid_character=lambda x: False,
        signal=set_signal,

        is_terminating_macro_character=lambda x: False,
        read_token_even_dispatch_handle_terminating_macro_character=lambda state, current, read, stream, x: "handle-terminating-macro",

        is_whitespace_character=lambda x: False,
        read_token_even_dispatch_handle_whitespace_character=lambda state, current, read, stream, x: "handle-whitespace"
    )
    state = {
        "signal": None
    }
    result = read.read_token_even_dispatch(n, state, None, None, None, "")
    assert result == None
    assert state["signal"] == "reader-error"

def test_read_token_even_dispatch_terminating_macro_character():
    n = SimpleNamespace(
        is_constituent_or_nonterminating_macro_character=lambda x: False,
        read_token_even_dispatch_handle_constituent_or_nonterminating_macro_character=lambda state, current, read, stream, x: "handle-constituent-or-nonterminating-macro",

        is_single_escape_character=lambda x: False,
        read_token_even_dispatch_handle_single_escape_character=lambda state, current, read, stream, x: "handle-single-escape",

        is_multiple_escape_character=lambda x: False,
        read_token_even_dispatch_handle_multiple_escape_character=lambda state, current, read, stream, x: "handle-multiple-escape",

        is_valid_character=lambda x: True,
        signal=set_signal,

        is_terminating_macro_character=lambda x: True,
        read_token_even_dispatch_handle_terminating_macro_character=lambda state, current, read, stream, x: "handle-terminating-macro",

        is_whitespace_character=lambda x: False,
        read_token_even_dispatch_handle_whitespace_character=lambda state, current, read, stream, x: "handle-whitespace"
    )
    result = read.read_token_even_dispatch(n, None, None, None, None, "")
    assert result == "handle-terminating-macro"

def test_read_token_even_dispatch_whitespace_character():
    n = SimpleNamespace(
        is_constituent_or_nonterminating_macro_character=lambda x: False,
        read_token_even_dispatch_handle_constituent_or_nonterminating_macro_character=lambda state, current, read, stream, x: "handle-constituent-or-nonterminating-macro",

        is_single_escape_character=lambda x: False,
        read_token_even_dispatch_handle_single_escape_character=lambda state, current, read, stream, x: "handle-single-escape",

        is_multiple_escape_character=lambda x: False,
        read_token_even_dispatch_handle_multiple_escape_character=lambda state, current, read, stream, x: "handle-multiple-escape",

        is_valid_character=lambda x: True,
        signal=set_signal,

        is_terminating_macro_character=lambda x: False,
        read_token_even_dispatch_handle_terminating_macro_character=lambda state, current, read, stream, x: "handle-terminating-macro",

        is_whitespace_character=lambda x: True,
        read_token_even_dispatch_handle_whitespace_character=lambda state, current, read, stream, x: "handle-whitespace"
    )
    result = read.read_token_even_dispatch(n, None, None, None, None, "")
    assert result == "handle-whitespace"

def test_read_token_even_dispatch_handle_constituent_or_nonterminating_macro_character():
    n = SimpleNamespace(
        apply_readtable_case=lambda y: y
    )
    current = {
        "token": "A"
    }
    result = read.read_token_even_dispatch_handle_constituent_or_nonterminating_macro_character(n, None, current, None, None, "B")
    assert result == None
    assert current["token"] == "AB"

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
    stream = streams.create("")
    result = read.read(n, None, stream)
    assert result == "eof"

def test_read_return_value():
    save_inputs = []
    n = SimpleNamespace(
        handle_end_of_file=None,
        read_dispatch=create_fake_read_dispatch(save_inputs),
    )
    state = {
        "signal": None
    }
    stream = streams.create("abcR")
    result = read.read(n, state, stream)
    assert save_inputs == ["a", "b", "c", "R"]
    assert result == "abcR"
    assert state["signal"] == None

def test_read_signal():
    save_inputs = []
    n = SimpleNamespace(
        handle_end_of_file=None,
        read_dispatch=create_fake_read_dispatch(save_inputs),
    )
    state = {
        "signal": None
    }
    stream = streams.create("abcSxyz")
    result = read.read(n, state, stream)
    assert save_inputs == ["a", "b", "c", "S"]
    assert not result
    assert state["signal"] == "fake-signal"

def run_tests():
    test_read_dispatch_invalid_character()
    test_read_dispatch_whitespace_character()
    test_read_dispatch_macro_character()
    test_read_dispatch_single_escape_character()
    test_read_dispatch_multiple_escape_character()
    test_read_dispatch_constituent_character()

    test_read_dispatch_handle_whitespace_character()
    test_read_dispatch_handle_macro_character()
    test_read_dispatch_handle_single_escape_character()
    test_read_dispatch_handle_multiple_escape_character()
    test_read_dispatch_handle_constituent_character()

    test_read_token_even_dispatch_constituent_or_nonterminating_macro_character()
    test_read_token_even_dispatch_single_escape_character()
    test_read_token_even_dispatch_multiple_escape_character()
    test_read_token_even_dispatch_invalid_character()
    test_read_token_even_dispatch_terminating_macro_character()
    test_read_token_even_dispatch_whitespace_character()

    test_read_token_even_dispatch_handle_constituent_or_nonterminating_macro_character()

    # create tests for read_token_{even,odd} handlers

    test_read_token()

    test_read_end_of_file()
    test_read_return_value()
    test_read_signal()

    print("test_read : passed")
