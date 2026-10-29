import streams
from character import \
    is_constituent, \
    is_macro, \
    is_terminating_macro, \
    is_nonterminating_macro, \
    is_whitespace_character

def read_token_even_dispatch_handle_constituent_or_nonterminating_macro_character(n, state, current, read, stream, y):
    current["token"] += n.apply_readtable_case(y)
    return

def read_token_even_dispatch(n, state, current, read, stream, y):
    if n.is_constituent_or_nonterminating_macro_character(y):
        return n.read_token_even_dispatch_handle_constituent_or_nonterminating_macro_character(state, current, read, stream, y)
    elif n.is_single_escape_character(y):
        return n.read_token_even_dispatch_handle_single_escape_character(state, current, read, stream, y)
    elif n.is_multiple_escape_character(y):
        return n.read_token_even_dispatch_handle_multiple_escape_character(state, current, read, stream, y)
    elif not n.is_valid_character(y):
        n.signal(state, "reader-error")
        return None
    elif n.is_terminating_macro_character(y):
        return n.read_token_even_dispatch_handle_terminating_macro_character(state, current, read, stream, y)
    elif n.is_whitespace_character(y):
        return n.read_token_even_dispatch_handle_whitespace_character(state, current, read, stream, y)

# CREATE TESTS FOR THIS
def read_token_dispatch(n, state, current, stream, y):
    if current["status"] == "even":
        return n.read_token_even_dispatch(state, current, y)
    else:
        return n.read_token_odd_dispatch(state, current, y)

def read_token(n, state, initial_status, stream, token_initializer):
    current = {
        "status": initial_status,
        "token": token_initializer
    }
    y = streams.get_next_character(stream)
    while y:
        result = n.read_token_dispatch(state, current, stream, y)
        if result:
            return result
        if state["signal"]:
            return None
        y = streams.get_next_character(stream)
    return n.handle_end_of_file()

def skip_whitespace(stream):
    x = streams.see_next_character(stream)
    while is_whitespace_character(x):
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

def read_dispatch_handle_whitespace_character(n, state, read, stream, x):
    return None

def read_dispatch_handle_macro_character(n, state, read, stream, x):
    reader_macro_function = n.get_reader_macro_function(read, x)
    return reader_macro_function(stream, x)

def read_dispatch_handle_single_escape_character(n, state, read, stream, x):
    y = streams.get_next_character(stream)
    if not y:
        n.signal(state, "end-of-file")
        return None
    return n.read_token(state, "even", stream, y)

def read_dispatch_handle_multiple_escape_character(n, state, read, stream, x):
    return n.read_token(state, "odd", stream, "")

def read_dispatch_handle_constituent_character(n, state, read, stream, x):
    return n.read_token(state, "even", stream, x)

def read_dispatch(n, state, read, stream, x):
    if n.is_whitespace_character(x):
        return n.read_dispatch_handle_whitespace_character(state, read, stream, x)
    elif n.is_macro(x):
        return n.read_dispatch_handle_macro_character(state, read, stream, x)
    elif n.is_single_escape(x):
        return n.read_dispatch_handle_single_escape(state, read, stream, x)
    elif n.is_multiple_escape(x):
        return n.read_dispatch_handle_multiple_escape(state, read, stream, x)
    elif n.is_constituent(x):
        return n.read_dispatch_handle_constituent(state, read, stream, x)
    elif not n.is_valid(x):
        n.signal(state, "reader-error")
        return None

def read(n, state, stream):
    x = streams.get_next_character(stream)
    while x:
        result = n.read_dispatch(state, read, stream, x)
        if result:
            return result
        if state["signal"]:
            return None
        x = streams.get_next_character(stream)
    return n.handle_end_of_file()
