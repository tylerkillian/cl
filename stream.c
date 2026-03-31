#include <file.h>
#include <stdio.h>
#include <stream.h>
#include <string.h>

stream_t* stream_create(memory_t *memory, char *filename) {
	stream_t *stream;
	stream = (stream_t*)memory_malloc(memory, sizeof(stream_t));
	stream->memory = memory;
	stream->buffer = read_file(memory, filename);
	printf("%s", stream->buffer);
	return stream;
}

void stream_destroy(stream_t *stream) {
	memory_free(stream->memory, stream->buffer);
	memory_free(stream->memory, stream);
}

char stream_get_next_character(stream_t *stream) {
	int current_length;
	char *buffer, next_character;

	current_length = strlen(stream->buffer);
	if (current_length > 0) {
		next_character = stream->buffer[0];

		buffer = (char*)memory_malloc(stream->memory, current_length * sizeof(char));
		strcpy(buffer, &stream->buffer[1]);
		memory_free(stream->memory, stream->buffer);
		stream->buffer = buffer;

		return next_character;
	} else {
		return EOF;
	}
}

void stream_prepend(stream_t *stream, char c) {
        int current_length;
        char *buffer;

        current_length = strlen(stream->buffer);
        buffer = (char*)memory_malloc(stream->memory, (current_length + 2) * sizeof(char));
        buffer[0] = c;
        strcpy(buffer + 1, stream->buffer);
        memory_free(stream->memory, stream->buffer);
        stream->buffer = buffer;
}
