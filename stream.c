#include <file.h>
#include <stdio.h>
#include <stream.h>

Stream* Stream_create(Memory *memory, char *filename) {
	Stream *stream;
	stream = (Stream*)Memory_malloc(memory, sizeof(Stream));
	stream->memory = memory;
	stream->contents = read_file(memory, filename);
	printf("%s", stream->contents);
	return stream;
}

void Stream_destroy(Stream *stream) {
	Memory_free(stream->memory, stream->contents);
	Memory_free(stream->memory, stream);
}
