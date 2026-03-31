#include <assert.h>
#include <cl.h>
#include <memory.h>
#include <stdio.h>
#include <test_repl.h>

int main(int argc, char **argv) {
	char *filename;
	memory_t *memory;
	
	assert(argc == 2);
	filename = argv[1];

	memory = memory_create();

	cl_load(memory, filename);

	memory_assert_empty(memory);
	memory_destroy(memory);
	return 0;
}
