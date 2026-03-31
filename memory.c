#include <assert.h>
#include <memory.h>
#include <string.h>

memory_t* memory_create() {
	memory_t *memory;

	memory = (memory_t*)malloc(sizeof(memory_t));
	memory->blocks = NULL;
	memory->num_blocks = 0;

	return memory;
}

void memory_destroy(memory_t *memory) {
	free(memory);
}

void _add_block(memory_t *memory, void *ptr) {
        void **blocks;

        blocks = (void**)malloc((memory->num_blocks + 1) * sizeof(void*));
        memcpy(blocks, memory->blocks, memory->num_blocks * sizeof(void*));
        blocks[memory->num_blocks] = ptr;

        if (memory->blocks != NULL) {
                free(memory->blocks);
        }

        memory->blocks = blocks;
        memory->num_blocks++;
}

void* memory_malloc(memory_t *memory, size_t size) {
	void *result;

	result = malloc(size);

	_add_block(memory, result);

	return result;
}

void _remove_block(memory_t *memory, void *ptr) {
        int index;
        void **blocks;

        index = -1;
        for (index = 0; index < memory->num_blocks; index++) {
                if (memory->blocks[index] == ptr) {
                        break;
                }
        }
        assert(index >= 0);

        if (memory->num_blocks > 1) {
                blocks = (void**)malloc((memory->num_blocks - 1) * sizeof(void*));
        } else {
                blocks = NULL;
        }

        memcpy(blocks, memory->blocks, index * sizeof(void*));
        memcpy(blocks + index, memory->blocks + index + 1, (memory->num_blocks - index - 1) * sizeof(void*));

        free(memory->blocks);

        memory->blocks = blocks;
        memory->num_blocks--;
}

void memory_free(memory_t *memory, void *block) {
	_remove_block(memory, block);
	free(block);
}

void memory_assert_empty(memory_t *memory) {
        assert(memory->num_blocks == 0);
        assert(memory->blocks == NULL);
}
