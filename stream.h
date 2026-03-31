#ifndef _STREAM_H_
#define _STREAM_H_

#include <memory.h>

typedef struct {
	memory_t *memory;
	char *buffer;
} stream_t;

stream_t* stream_create(memory_t *memory, char *filename);
void stream_destroy(stream_t *stream);
char stream_get_next_character(stream_t *stream);
void stream_prepend(stream_t *s, char c);

#endif
