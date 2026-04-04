#include <object.h>
#include <stdio.h>
#include <stdlib.h>

object_t* object_create(memory_t *memory) {
        object_t *object;
        object = (object_t*)memory_malloc(memory, sizeof(object_t));
        object->memory = memory;
	object->type = SYMBOL;
	object->data = NULL;
        return object;
}

void object_destroy(object_t *object) {
        memory_free(object->memory, object);
}

object_t* object_interpret_token(memory_t *memory, string_t *token) {
	object_t *result;

	printf("Interpreting %s\n", token->buffer);

	result = object_create(memory);
	return result;
}

void object_print(object_t *object) {
	if (object) {
		return;
	}
}

boolean object_is_nil(object_t *object) {
	if (object->data == NULL) {
		return TRUE;
	} else {
		return FALSE;
	}
}
