#include <file.h>
#include <stdio.h>

char* read_file(Memory *memory, char *filename) {
	int num_characters, character_index;
	char c, *result;
	FILE *file;

	file = fopen(filename, "r");
	num_characters = 0;
	c = fgetc(file);
	while (c != EOF) {
		num_characters++;
		c = fgetc(file);
	}
	fclose(file);

	result = (char*)Memory_malloc(memory, (num_characters + 1) * sizeof(char));

	file = fopen(filename, "r");
	character_index = 0;
	c = fgetc(file);
	while (c != EOF) {
		result[character_index] = c;
		c = fgetc(file);
		character_index++;
	}
	fclose(file);

	result[num_characters] = '\0';

	return result;
}
