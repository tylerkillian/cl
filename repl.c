#include <repl.h>

#include <assert.h>
void repl(
	object_t* (*read_ptr)(void*, memory_t*, stream_t*),
	void *read_data,
	value_t* (*eval_ptr)(memory_t *memory, object_t *form),
	void (*print_ptr)(value_t *value),
	memory_t *memory, 
	stream_t *stream
) {
	object_t *object;
	value_t *value;

	value = NULL;
	assert(value == NULL);
	assert(eval_ptr);
	assert(print_ptr);
	assert(memory != NULL);

	object = read_ptr(read_data, memory, stream);
	while (object->object_type != NIL) {
		value = eval_ptr(memory, object);
		object_destroy(object);

		print_ptr(value);
		value_destroy(value);
	}
	object_destroy(object);
}
