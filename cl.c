#include <cl.h>
#include <eval.h>
#include <print.h>
#include <read.h>
#include <stdio.h>
#include <stream.h>
#include <value.h>

void cl_load(memory_t *memory, char *filename) {
	object_t *object;
	value_t *value;
	stream_t *stream;

	stream = stream_create(memory, filename);
	object = read(memory, stream);
	value = eval(memory, object);
	print(value);
	object_print(object);
	object_destroy(object);
	stream_destroy(stream);
}
