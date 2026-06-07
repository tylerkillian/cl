import streams
from character import \
    is_constituent, \
    is_macro, \
    is_terminating_macro, \
    is_whitespace

def read_token(stream):
    result = ""
    while True:
        if streams.at_end_of_file(stream):
            return result

        y = streams.get_next_character(stream)
        if is_constituent(y):
            result += y
        elif is_whitespace(y):
            return result
        elif is_terminating_macro(y):
            streams.prepend(stream, y)
            return result
        else:
            assert False

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

def handle_constituent(read, stream, x):
    return x + read_token(stream)

def read_dispatch(n, read, stream, x):
    if n.is_whitespace(x):
        return n.handle_whitespace(read, stream, x)
    elif n.is_macro(x):
        return n.handle_macro_character(read, stream, x)
    elif n.is_constituent(x):
        return n.handle_constituent(read, stream, x)
    elif not n.is_valid(x):
        return n.signal("reader-error")

def read(n, stream):
    x = streams.get_next_character(stream)
    while x:
        result = n.read_dispatch(n.dispatch, read, stream, x)
        if result:
            return result
        x = streams.get_next_character(stream)
    return n.handle_end_of_file()
