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
	int currentLength;
	char *buffer, nextCharacter;

	currentLength = strlen(stream->buffer);
	if (currentLength > 0) {
		nextCharacter = stream->buffer[0];

		buffer = (char*)memory_malloc(stream->memory, currentLength * sizeof(char));
		strcpy(buffer, &stream->buffer[1]);
		memory_free(stream->memory, stream->buffer);
		stream->buffer = buffer;

		return nextCharacter;
	} else {
		return EOF;
	}
}

void stream_prepend(stream_t *stream, char c) {
        int currentLength;
        char *buffer;

        currentLength = strlen(stream->buffer);
        buffer = (char*)memory_malloc(stream->memory, (currentLength + 2) * sizeof(char));
        buffer[0] = c;
        strcpy(buffer + 1, stream->buffer);
        memory_free(stream->memory, stream->buffer);
        stream->buffer = buffer;
}
