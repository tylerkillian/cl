#include <eval.h>

#include <assert.h>
value_t* eval(memory_t *memory, object_t *form) {
	value_t *result;

	assert(form != NULL);

	result = value_create(memory);
	return result;
}
