#include <cl.h>
#include <stdio.h>
#include <stream.h>

void cl_load(Memory *memory, char *filename) {
	Stream *stream;

	printf("Loading %s\n", filename);

	stream = Stream_create(memory, filename);
	Stream_destroy(stream);
}
