#ifndef _MEMORY_H_
#define _MEMORY_H_

#include <stdlib.h>

typedef struct {
	int num_blocks;
	void **blocks;
} memory_t;

memory_t* memory_create();
void memory_destroy(memory_t *memory);

void* memory_malloc(memory_t *memory, size_t size);
void memory_free(memory_t *memory, void *block);

void memory_assert_empty(memory_t *memory);

#endif
