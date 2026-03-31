#include <boolean.h>
#include <read.h>
#include <stdio.h>
#include <str.h>

boolean isWhitespace(char c) {
	if (c == ' ') {
		return TRUE;
	} else {
		return FALSE;
	}
}

boolean isConstituent(char c) {
	if (isWhitespace(c)) {
		return FALSE;
	} else {
		return TRUE;
	}
}

string_t* _readToken(memory_t *memory, stream_t *stream) {
	char x;
	string_t *result;

	result = string_create(memory);
	x = stream_get_next_character(stream);
	while (x != EOF) {
		if (isConstituent(x)) {
			string_append(result, x);
		} else if (isWhitespace(x)) {
			break;
		} else {
			stream_prepend(stream, x);
			break;
		}
		x = stream_get_next_character(stream);
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

object_t* read(memory_t *memory, stream_t *stream) {
	char x;
	string_t *token;
	object_t *result;

	result = NULL;

	x = stream_get_next_character(stream);
	while (x != EOF) {
		printf("[%c]\n", x);
		if (isWhitespace(x)) {
			printf("got whitespace\n");
		} else if (x == '(') {
		} else if (isConstituent(x)) {
			token = _readToken(memory, stream);
			string_prepend(token, x);
			printf("x = %c ; token = %s\n", x, token->buffer);
			result = object_interpret_token(memory, token);
			string_destroy(token);
			break;
		} else {
		}
		x = stream_get_next_character(stream);
	}

	if (result) {
		return result;
	} else {
		return object_create(memory);
	}
}
