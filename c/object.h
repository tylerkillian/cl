#ifndef _OBJECT_H_
#define _OBJECT_H_

#include <boolean.h>
#include <str.h>

typedef enum {
	SYMBOL,
	CONS,
	NUMBER
} object_type_e;

typedef struct {
	memory_t *memory;
	object_type_e type;
	void *data;
} object_t;

object_t* object_create(memory_t *memory);
void object_destroy(object_t *object);
object_t* object_interpret_token(memory_t *memory, string_t *token);
void object_print(object_t *object);
boolean object_is_nil(object_t *object);

#endif
