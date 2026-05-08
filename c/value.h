#ifndef _VALUE_H_
#define _VALUE_H_

#include <memory.h>

typedef struct {
	memory_t *memory;
} value_t;

value_t* value_create(memory_t *memory);
void value_destroy(value_t *value);

#endif
