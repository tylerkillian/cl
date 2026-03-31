#ifndef _STR_H_
#define _STR_H_

#include <memory.h>

typedef struct {
	memory_t *memory;
	char *buffer;
} string_t;

string_t* string_create(memory_t *memory);
void string_destroy(string_t* s);
void string_prepend(string_t *s, char c);
void string_append(string_t *s, char c);

#endif
