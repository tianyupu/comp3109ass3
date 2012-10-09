#include "head.h"

extern void test0(long, float *);

int main(void) {
  float *a = malloc(sizeof(float)*NUM  + SSE_ALIGN);

  // make sure that pointers are aligned to multiples of 16 bytes
  a = (float *) align(a, SSE_ALIGN);

  // write values to a and b
  // and invoke the function written in the vector language
  // and read values from c
  
  // test 0
  *a = 1;
  test0(NUM, a);
  printf("0: a = %f\n", *a);
  
  return 0;
}
