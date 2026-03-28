#ifndef _OBJECT_H_
#define _OBJECT_H_

#include <str.h>

typedef enum {
	NUMBER,
	SYMBOL,
	NIL
} ObjectType;

typedef struct {
	Memory *memory;
	ObjectType type;
} Object;

Object* Object_create(Memory *memory);
void Object_destroy(Object *object);
Object* Object_interpretToken(Memory *memory, String *token);
void Object_print(Object *object);

#endif
