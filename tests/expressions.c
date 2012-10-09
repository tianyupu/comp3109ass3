#include "head.h"

extern void test0(long, float *);
extern void test1(long, float *, float *);
extern void test2(long, float *, float *);

int main(void) {
  float *a = createvect(NUM),
        *b = createvect(NUM);

  // test 0
  setvect(NUM, a, 1);
  test0(NUM, a);
  printf("0: a = %f, b = %f \n", *a, *b);
  
  // test 1
  setvect(NUM, a, 1);
  setvect(NUM, b, 0);
  test1(NUM, a, b);
  printf("1: a = %f, b = %f \n", *a, *b);
  
  // test 2
  setvect(NUM, a, 1);
  setvect(NUM, b, 0);
  test2(NUM, a, b);
  printf("2: a = %f, b = %f \n", *a, *b);
  
  return 0;
}
