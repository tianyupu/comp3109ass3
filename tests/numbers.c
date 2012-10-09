#include "head.h"

extern void test0(long, float *);
extern void test1(long, float *, float *);
extern void test2(long, float *, float *);
extern void test3(long, float *, float *);
extern void test4(long, float *, float *);

int main(void) {
  float *a = malloc(sizeof(float)*NUM + SSE_ALIGN),
        *b = malloc(sizeof(float)*NUM + SSE_ALIGN);

  // make sure that pointers are aligned to multiples of 16 bytes
  a = (float *) align(a, SSE_ALIGN);

  // write values to a and b
  // and invoke the function written in the vector language
  // and read values from c
  
  // test 0
  *a = 1;
  test0(NUM, a);
  printf("0: a = %f \n", *a);
  
  // test 1
  *a = 1;
  test1(NUM, a, b);
  printf("1: a = %f \n", *a);
  
  // test 2
  *a = 1;
  test2(NUM, a, b);
  printf("2: a = %f \n", *a);
  
  // test 3
  *a = 1;
  test3(NUM, a, b);
  printf("3: a = %f \n", *a);
  
  // test 4
  *a = 1;
  test4(NUM, a, b);
  printf("4: a = %f \n", *a);

  return 0;
}
