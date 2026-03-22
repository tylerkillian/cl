#ifndef _STREAM_H_
#define _STREAM_H_

#include <memory.h>

typedef struct {
	Memory *memory;
	char *buffer;
} Stream;

Stream* Stream_create(Memory *memory, char *filename);
char Stream_getNextCharacter(Stream *stream);
void Stream_destroy(Stream *stream);

#endif
