#include <test_repl.h>
#include <repl.h>
#include <stdlib.h>

#include <assert.h>
object_t* _read(void *count, memory_t *memory, stream_t *stream) {
	object_t *result;

	assert(*(int*)count == 0);
	assert(stream == NULL);

	result = object_create(memory);
	return result;
}

value_t* _eval(memory_t *memory, object_t *form) {
	value_t *result;

	assert(form == NULL);

	result = value_create(memory);
	return result;
}

void _print(value_t *value) {
	assert(value == NULL);
}

void test_repl(memory_t *memory) {
	int count;

	assert(memory != NULL);

	count = 0;
	assert(count == 0);

	repl(_read, &count, _eval, _print, memory, NULL);
}
