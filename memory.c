#include <memory.h>

Memory* Memory_create() {
	Memory *memory;

	memory = (Memory*)malloc(sizeof(Memory));
	memory->blocks = NULL;
	memory->num_blocks = 0;

	return memory;
}

void Memory_destroy(Memory *memory) {
	free(memory);
}

void* Memory_malloc(Memory *memory, size_t size) {
	void *result;

	memory->num_blocks++;

	result = malloc(size);
	return result;
}

void Memory_free(Memory *memory, void *block) {
	memory->num_blocks--;
	free(block);
}
