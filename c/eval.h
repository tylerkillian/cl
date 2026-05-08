#ifndef _EVAL_H_
#define _EVAL_H_

#include <memory.h>
#include <object.h>
#include <value.h>

value_t* eval(memory_t *memory, object_t *form);

#endif
