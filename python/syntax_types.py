SYNTAX_TYPES = [
    "constituent",
    "macro",
    "character",
    "single",
    "escape",
    "invalid",
    "multiple",
    "escape",
    "whitespace"
]

RUBOUT_CHARACTER = chr(127)
BACKSPACE_CHARACTER = chr(8)
PROGRAMMER_CONSTITUENT_CHARACTERS = "?![]{}"
CONSTITUENT_CHARACTERS = \
    "0123456789:<=>@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz$%&^_*+-~./" \
    + PROGRAMMER_CONSTITUENT_CHARACTERS \
    + RUBOUT_CHARACTER \
    + BACKSPACE_CHARACTER

TERMINATING_MACRO_CHARACTERS = ";'(`)\","

NON_TERMINATING_MACRO_CHARACTER = "#"

TAB = chr(9)
NEWLINE = chr(10)
LINEFEED = chr(10)
PAGE = chr(12)
RETURN = chr(13)
SPACE = chr(32)
WHITESPACE = TAB + NEWLINE + LINEFEED + PAGE + RETURN + SPACE

SINGLE_ESCAPE = "\\"

MULTIPLE_ESCAPE = "|"

def is_constituent(c):
    if c in CONSTITUENT_CHARACTERS:
        return True
    else:
        return False

def is_non_terminating_macro(c):
    if c == NON_TERMINATING_MACRO_CHARACTER:
        return True
    else:
        return False

def is_whitespace(c):
    if c in WHITESPACE:
        return True
    else:
        return False

def is_single_escape(c):
    if c == SINGLE_ESCAPE:
        return True
    else:
        return False

def is_multiple_escape(c):
    if c == MULTIPLE_ESCAPE:
        return True
    else:
        return False
