#include <string.h>
#include <str.h>

String* String_create(Memory *memory) {
	String *s;
        s = (String*)Memory_malloc(memory, sizeof(String));
        s->memory = memory;
        s->buffer = (char*)Memory_malloc(memory, sizeof(char));
	s->buffer[0] = '\0';
        return s;
}

void String_destroy(String *s) {
	Memory_free(s->memory, s->buffer);
        Memory_free(s->memory, s);
}

void String_prepend(String *s, char c) {
	int currentLength;
	char *buffer;

	currentLength = strlen(s->buffer);
	buffer = (char*)Memory_malloc(s->memory, (currentLength + 2) * sizeof(char));
	buffer[0] = c;
	strcpy(buffer + 1, s->buffer);
	Memory_free(s->memory, s->buffer);
	s->buffer = buffer;
}

void String_append(String *s, char c) {
	int currentLength;
	char *buffer;

	currentLength = strlen(s->buffer);
	buffer = (char*)Memory_malloc(s->memory, (currentLength + 2) * sizeof(char));
	strcpy(buffer, s->buffer);
	buffer[currentLength] = c;
	Memory_free(s->memory, s->buffer);
	s->buffer = buffer;
}
