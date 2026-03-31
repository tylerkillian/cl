#include <string.h>
#include <str.h>

string_t* string_create(memory_t *memory) {
	string_t *s;
        s = (string_t*)memory_malloc(memory, sizeof(string_t));
        s->memory = memory;
        s->buffer = (char*)memory_malloc(memory, sizeof(char));
	s->buffer[0] = '\0';
        return s;
}

void string_destroy(string_t *s) {
	memory_free(s->memory, s->buffer);
        memory_free(s->memory, s);
}

void string_prepend(string_t *s, char c) {
	int current_length;
	char *buffer;

	current_length = strlen(s->buffer);
	buffer = (char*)memory_malloc(s->memory, (current_length + 2) * sizeof(char));
	buffer[0] = c;
	strcpy(buffer + 1, s->buffer);
	memory_free(s->memory, s->buffer);
	s->buffer = buffer;
}

void string_append(string_t *s, char c) {
	int current_length;
	char *buffer;

	current_length = strlen(s->buffer);
	buffer = (char*)memory_malloc(s->memory, (current_length + 2) * sizeof(char));
	strcpy(buffer, s->buffer);
	buffer[current_length] = c;
	memory_free(s->memory, s->buffer);
	s->buffer = buffer;
}
