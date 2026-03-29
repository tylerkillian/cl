#include <cl.h>
#include <eval.h>
#include <print.h>
#include <read.h>
#include <stdio.h>
#include <stream.h>
#include <value.h>

void cl_load(Memory *memory, char *filename) {
	Object *object;
	Value *value;
	Stream *stream;

	printf("Loading %s\n", filename);

	stream = Stream_create(memory, filename);
	object = read(memory, stream);
	value = eval(object);
	print(value);
	Object_print(object);
	Object_destroy(object);
	Stream_destroy(stream);
}
