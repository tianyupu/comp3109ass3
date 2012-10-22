#include <stdlib.h>
#include <stdio.h>

// our vector library
#include "vector.h"

// alignment macro: aligns a memory block a to multiples of a
#define align(s,a) (((size_t)(s) + ((a)-1)) & ~ ((size_t) (a) - 1))

// alignment for SSE unit
#define SSE_ALIGN (16)

// number of elements
#define NUM (4)
