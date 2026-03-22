#include <cl.h>
#include <read.h>
#include <stdio.h>
#include <stream.h>

void cl_load(Memory *memory, char *filename) {
	Object *object;
	Stream *stream;

	printf("Loading %s\n", filename);

	stream = Stream_create(memory, filename);
	object = read(memory, stream);
	Object_print(object);
	Stream_destroy(stream);
}
