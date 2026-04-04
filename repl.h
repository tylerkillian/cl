#ifndef _REPL_H_
#define _REPL_H_

#include <memory.h>
#include <object.h>
#include <stream.h>

void repl(
        object_t* (*read_ptr)(void*, memory_t*, stream_t*),
	void *read_data,
        object_t* (*eval_ptr)(void*, memory_t*, object_t*),
	void *eval_data,
        void (*print_ptr)(void*, object_t*),
	void *print_data,
        memory_t *memory,
        stream_t *stream
);

#endif
