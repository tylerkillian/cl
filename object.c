#include <object.h>
#include <stdio.h>

void Object_print(Object *object) {
	if (object) {
		printf("object type = %d\n", object->type);
	} else {
		printf("object is nil\n");
	}
}
