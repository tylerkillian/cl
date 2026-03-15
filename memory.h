#ifndef _MEMORY_H_
#define _MEMORY_H_

#include <stdlib.h>

typedef struct {
	int num_blocks;
	void **blocks;
} Memory;

Memory* Memory_create();
void Memory_destroy(Memory *memory);

void* Memory_malloc(Memory *memory, size_t size);
void Memory_free(Memory *memory, void *block);

void Memory_assert_empty(Memory *memory);

#endif
