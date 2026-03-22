#include <file.h>
#include <stdio.h>
#include <stream.h>
#include <string.h>

Stream* Stream_create(Memory *memory, char *filename) {
	Stream *stream;
	stream = (Stream*)Memory_malloc(memory, sizeof(Stream));
	stream->memory = memory;
	stream->buffer = read_file(memory, filename);
	printf("%s", stream->buffer);
	return stream;
}

char Stream_getNextCharacter(Stream *stream) {
	int currentLength;
	char *buffer, nextCharacter;

	currentLength = strlen(stream->buffer);
	if (currentLength > 0) {
		nextCharacter = stream->buffer[0];

		buffer = (char*)Memory_malloc(stream->memory, currentLength * sizeof(char));
		strcpy(buffer, &stream->buffer[1]);
		Memory_free(stream->memory, stream->buffer);
		stream->buffer = buffer;

		return nextCharacter;
	} else {
		return EOF;
	}
}

void Stream_destroy(Stream *stream) {
	Memory_free(stream->memory, stream->buffer);
	Memory_free(stream->memory, stream);
}
