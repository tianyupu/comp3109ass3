#include <stdlib.h>
#include <stdio.h>

/* alignment macro: aligns a memory block a to multiplies of a */ 
#define align(s,a) ((size_t)((s) + ((a) - 1)) & ~((size_t) (a) - 1)) 
/* Alignment for SSE unit */ 
#define SSE_ALIGN (16) 
/* Number of elements */ 
#define NUM (16)

extern void foobar(int, float *, float *, float *);

void 
output_vector(const char name, float *const vector) {
  int i;
  printf("| %c |", name);
  for (i = 0; i != NUM; i++)
    printf(" %6.2f |", vector[i]);
  printf("\n");
  fflush(stdout);
}


int 
main(void) {
  int i;
  float *a = malloc(sizeof(float)*NUM + SSE_ALIGN);
  float *b = malloc(sizeof(float)*NUM + SSE_ALIGN);
  float *c = malloc(sizeof(float)*NUM + SSE_ALIGN);

  /* make sure that pointers are aligned to multiplies of 16 bytes */ 
  a = (float *)align(a, SSE_ALIGN); 
  b = (float *)align(b, SSE_ALIGN); 
  c = (float *)align(c, SSE_ALIGN);

  /* initialise a and b to arbitary values */
  for (i = 0; i != NUM; i++) {
    a[i] = i;
    b[i] = NUM - i - 1;
  }
  
  /* call the function(s) implemented in the VPL */
  foobar(NUM, a, b, c);
  
  /* print out the resultant values of the vectors */
  output_vector('a', a);
  output_vector('b', b);
  output_vector('c', c);

  return EXIT_SUCCESS;
}

