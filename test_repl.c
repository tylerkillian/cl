#include <test_repl.h>
#include <repl.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct {
	int index;
	object_t *save[4];
	char result[10];
} _data_t;

int _NOT_NULL;

#include <assert.h>
object_t* _read(void *data_v, memory_t *memory, stream_t *stream) {
	object_t *result;
	_data_t *data;

	assert(stream == NULL);

	data = (_data_t*)data_v;

	result = object_create(memory);
	data->save[data->index] = result;

	if (data->index < 3) {
		result->type = NUMBER;
		result->data = &_NOT_NULL;
		data->result[3 * data->index] = 'r';
	} else {
		result->type = NUMBER;
		result->data = NULL;
	}

	return result;
}

object_t* _eval(void *data_v, memory_t *memory, object_t *form) {
	_data_t *data;

	assert(data_v != NULL);
	assert(memory != NULL);
	assert(form->type == NUMBER);

	data = (_data_t*)data_v;

	data->result[3 * data->index + 1] = 'e';

	return form;
}

void _print(void *data_v, object_t *value) {
	_data_t *data;

	assert(data_v != NULL);
	assert(value != NULL);

	data = (_data_t*)data_v;

	data->result[3 * data->index + 2] = 'p';

	data->index++;
}

void test_repl(memory_t *memory) {
	int index;
	_data_t data;

	assert(memory != NULL);

	printf("test_repl : ");

	data.index = 0;
	data.result[9] = '\0';

	repl(_read, &data, _eval, &data, _print, &data, memory, NULL);

	for (index = 0; index < 4; index++) {
		object_destroy(data.save[index]);
	}

	assert(strcmp(data.result, "repreprep") == 0);

	printf("PASSED\n");
}
