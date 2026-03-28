#include <object.h>
#include <stdio.h>

Object* Object_create(Memory *memory) {
        Object *object;
        object = (Object*)Memory_malloc(memory, sizeof(Object));
        object->memory = memory;
	object->type = NIL;
        return object;
}

void Object_destroy(Object *object) {
        Memory_free(object->memory, object);
}

Object* Object_interpretToken(Memory *memory, String *token) {
	Object *result;

	printf("Interpreting %s\n", token->buffer);

	result = Object_create(memory);
	result->type = SYMBOL;
	return result;
}

void Object_print(Object *object) {
	if (object) {
		printf("object type = %d\n", object->type);
	} else {
		printf("object is nil\n");
	}
}
