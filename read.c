#include <boolean.h>
#include <read.h>
#include <stdio.h>
#include <str.h>

Boolean isWhitespace(char c) {
	if (c == ' ') {
		return TRUE;
	} else {
		return FALSE;
	}
}

Boolean isConstituent(char c) {
	if (isWhitespace(c)) {
		return FALSE;
	} else {
		return TRUE;
	}
}

String* _readToken(Memory *memory, Stream *stream) {
	char x;
	String *result;

	result = String_create(memory);
	x = Stream_getNextCharacter(stream);
	while (x != EOF) {
		if (isConstituent(x)) {
			String_append(result, x);
		} else if (isWhitespace(x)) {
			break;
		} else {
			Stream_prepend(stream, x);
			break;
		}
		x = Stream_getNextCharacter(stream);
	}
	return result;

/*
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
	    */
}

Object* read(Memory *memory, Stream *stream) {
	char x;
	String *token;
	Object *result;

	result = NULL;

	x = Stream_getNextCharacter(stream);
	while (x != EOF) {
		printf("[%c]\n", x);
		if (isWhitespace(x)) {
			printf("got whitespace\n");
		} else if (isConstituent(x)) {
			token = _readToken(memory, stream);
			String_prepend(token, x);
			printf("x = %c ; token = %s\n", x, token->buffer);
			result = Object_interpretToken(memory, token);
			String_destroy(token);
			break;
		} else {
		}
		x = Stream_getNextCharacter(stream);
	}

	if (result) {
		return result;
	} else {
		return Object_create(memory);
	}
}
