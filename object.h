#ifndef _OBJECT_H_
#define _OBJECT_H_

typedef enum {
	TOKEN
} ObjectType;

typedef struct {
	ObjectType type;
} Object;

void Object_print(Object *object);

#endif
