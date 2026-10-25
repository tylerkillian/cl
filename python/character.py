def is_whitespace_character(x):
    return x in " \n"

def is_macro(x):
    return x in '()"'

def is_terminating_macro(x):
    return x in ")"

def is_nonterminating_macro(x):
    return is_macro(x) and not is_terminating_macro(x)

def is_constituent(x):
    return not is_whitespace(x) and not is_macro(x)
