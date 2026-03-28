#ifndef _STREAM_H_
#define _STREAM_H_

#include <memory.h>

typedef struct {
	Memory *memory;
	char *buffer;
} Stream;

Stream* Stream_create(Memory *memory, char *filename);
void Stream_destroy(Stream *stream);
char Stream_getNextCharacter(Stream *stream);
void Stream_prepend(Stream *s, char c);

#endif
