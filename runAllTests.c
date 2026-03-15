#include <assert.h>
#include <stdio.h>

int main(int argc, char **argv) {
	char *filename;
	
	assert(argc == 2);

	filename = argv[1];

	printf("Running %s\n", filename);
	return 0;
}
