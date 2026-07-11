import streams
from character import \
    is_constituent, \
    is_macro, \
    is_terminating_macro, \
    is_whitespace

def read_token(n, state, read_token_state, stream):
    while True:
        if read_token_state["status"] == "even":
            n.read_token_even(state, read_token_state, stream)
        elif read_token_state["status"] == "odd":
            n.read_token_odd(state, read_token_state, stream)

        if read_token_state["status"] == "error":
            return
        elif read_token_state["status"] == "done":
            break

    n.handle_token_done(state, read_token_state)

def skip_whitespace(stream):
    x = streams.see_next_character(stream)
    while is_whitespace(x):
        streams.get_next_character(stream)
        x = streams.see_next_character(stream)

def read_s_expression(read, stream, x):
    assert x == "("
    result = []
    skip_whitespace(stream)
    while streams.see_next_character(stream) != ")":
        result.append(read(stream))
        skip_whitespace(stream)
    streams.get_next_character(stream)
    return result

def read_string(stream, x):
    assert x == '"'
    result = ""
    while True:
        next_character = streams.get_next_character(stream)
        if next_character == '"':
            break
        result += next_character
    return result

def get_reader_macro_function(read, x):
    def _read_s_expression(stream, x):
        return read_s_expression(read, stream, x)
    if x == "(":
        return _read_s_expression
    elif x == "\"":
        return read_string

def handle_whitespace(read, stream, x):
    return None

def handle_macro_character(read, stream, x):
    reader_macro_function = get_reader_macro_function(read, x)
    reader_macro_result = reader_macro_function(stream, x)
    if reader_macro_result:
        return reader_macro_result
    else:
        return None

def handle_constituent(n, state, read, stream, x):
    read_token_state = {
        "status": "even",
        "token": x,
    }
    n.read_token(state, read_token_state, stream)

def read_dispatch(n, state, read, stream, x):
    if n.is_whitespace(x):
        n.handle_whitespace(state, read, stream, x)
    elif n.is_macro(x):
        n.handle_macro_character(state, read, stream, x)
    elif n.is_single_escape(x):
        n.handle_single_escape(state, read, stream, x)
    elif n.is_multiple_escape(x):
        n.handle_multiple_escape(state, read, stream, x)
    elif n.is_constituent(x):
        n.handle_constituent(state, read, stream, x)
    elif not n.is_valid(x):
        n.signal(state, "reader-error")

def read(n, stream):
    x = streams.get_next_character(stream)
    while x:
        result = n.read_dispatch(n.dispatch, read, stream, x)
        if result:
            return result
        x = streams.get_next_character(stream)
    return n.handle_end_of_file()
