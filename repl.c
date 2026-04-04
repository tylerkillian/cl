#include <repl.h>
#include <stdlib.h>

#include <assert.h>
void repl(
	object_t* (*read_ptr)(void*, memory_t*, stream_t*),
	void *read_data,
	object_t* (*eval_ptr)(void*, memory_t*, object_t*),
	void *eval_data,
	void (*print_ptr)(void*, object_t*),
	void *print_data,
	memory_t *memory, 
	stream_t *stream
) {
	object_t *object, *value;

	value = NULL;
	assert(value == NULL);
	assert(eval_ptr);
	assert(print_ptr);
	assert(memory != NULL);

	object = read_ptr(read_data, memory, stream);
	while (! object_is_nil(object)) {
		value = eval_ptr(eval_data, memory, object);
		print_ptr(print_data, value);

		object = read_ptr(read_data, memory, stream);
	}
}
