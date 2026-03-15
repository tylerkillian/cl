#ifndef _STREAM_H_
#define _STREAM_H_

#include <memory.h>

typedef struct {
	Memory *memory;
	char *contents;
} Stream;

Stream* Stream_create(Memory *memory, char *filename);
void Stream_destroy(Stream *stream);

#endif
