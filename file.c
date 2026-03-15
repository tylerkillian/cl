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
	result[num_characters] = '\0';

	file = fopen(filename, "r");
	character_index = 0;
	c = fgetc(file);
	while (c != EOF) {
		num_characters++;
		c = fgetc(file);
		result[character_index] = c;
		character_index++;
	}
	fclose(file);

	return result;
}
