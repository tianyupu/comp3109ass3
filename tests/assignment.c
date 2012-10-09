#include <stdlib.h>
#include <stdio.h>
// alignment macro: aligns a memory block a to multiples of a
#define align(s,a) (((size_t)(s) + ((a)-1)) & ~ ((size_t) (a) - 1))
// alignment for SSE unit
#define SSE_ALIGN (16)
// number of elements
#define NUM (4)

extern void test0(long, float *);
extern void test1(long, float *, float *);
extern void test2(long, float *, float *);
extern void test3(long, float *, float *);

int main(void) {
  float *a = malloc(sizeof(float)*NUM  + SSE_ALIGN),
        *b = malloc(sizeof(float)*NUM  + SSE_ALIGN);

  // make sure that pointers are aligned to multiples of 16 bytes
  a = (float *) align(a, SSE_ALIGN);
  b = (float *) align(b, SSE_ALIGN);

  // write values to a and b
  // and invoke the function written in the vector language
  // and read values from c
  
  // test 0
  //*a = 1; *b = 2;
  test0(NUM, a);
  printf("0: a = %f, b = %f \n", *a, *b);
  
  /*
  // test 1
  *a = 1; *b = 2;
  test1(NUM, a, b);
  printf("1: a = %f, b = %f \n", *a, *b);
  
  // test 2
  *a = 1; *b = 2;
  test2(NUM, a, b);
  printf("2: a = %f, b = %f \n", *a, *b);
  
  // test 3
  *a = 1; *b = 2;
  test3(NUM, a, b);
  printf("3: a = %f, b = %f \n", *a, *b);
  */

  return 0;
}
