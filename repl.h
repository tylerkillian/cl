#ifndef _REPL_H_
#define _REPL_H_

#include <memory.h>
#include <object.h>
#include <stream.h>
#include <value.h>

void repl(
        object_t* (*read_ptr)(void*, memory_t*, stream_t*),
	void *read_data,
        value_t* (*eval_ptr)(memory_t*, object_t*),
        void (*print_ptr)(value_t*),
        memory_t *memory,
        stream_t *stream
);

#endif
