#include <object.h>
#include <stdio.h>

object_t* object_create(memory_t *memory) {
        object_t *object;
        object = (object_t*)memory_malloc(memory, sizeof(object_t));
        object->memory = memory;
	object->object_type = NIL;
        return object;
}

void object_destroy(object_t *object) {
        memory_free(object->memory, object);
}

object_t* object_interpret_token(memory_t *memory, string_t *token) {
	object_t *result;

	printf("Interpreting %s\n", token->buffer);

	result = object_create(memory);
	result->object_type = SYMBOL;
	return result;
}

void object_print(object_t *object) {
	if (object) {
		return;
	}
}
