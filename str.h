#ifndef _STR_H_
#define _STR_H_

#include <memory.h>

typedef struct {
	Memory *memory;
	char *buffer;
} String;

String* String_create(Memory *memory);
void String_destroy(String* s);
void String_prepend(String *s, char c);
void String_append(String *s, char c);

#endif
