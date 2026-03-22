#include <read.h>
#include <stdio.h>

#include <assert.h>
Object* read(Memory *memory, Stream *stream) {
	char x;
	assert(memory);

	x = Stream_getNextCharacter(stream);
	while (x != EOF) {
		printf("[%c]\n", x);
		x = Stream_getNextCharacter(stream);
	}

	return NULL;
}
