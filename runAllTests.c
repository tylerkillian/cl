#include <assert.h>
#include <cl.h>
#include <memory.h>
#include <stdio.h>

int main(int argc, char **argv) {
	char *filename;
	Memory *memory;
	
	assert(argc == 2);
	filename = argv[1];

	memory = Memory_create();

	cl_load(memory, filename);

	Memory_destroy(memory);
	return 0;
}
