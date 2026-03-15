#include <stream.h>
#include <file.h>

Stream* Stream_create(Memory *memory, char *filename) {
	Stream *stream;
	stream = (Stream*)Memory_malloc(memory, sizeof(Stream));
	stream->memory = memory;
	stream->contents = read_file(memory, filename);
	return stream;
}

void Stream_destroy(Stream *stream) {
	Memory_free(stream->memory, stream);
}
