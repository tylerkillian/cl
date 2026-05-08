#include <value.h>
#include <stdlib.h>

#include <assert.h>
value_t* value_create(memory_t *memory) {
        value_t *value;

	assert(memory != NULL);

        value = (value_t*)memory_malloc(memory, sizeof(value_t));
        value->memory = memory;
        return value;
}

void value_destroy(value_t *value) {
        memory_free(value->memory, value);
}
