#include "head.h"

extern void test0(long, float *);
extern void test1(long, float *, float *);
extern void test2(long, float *);

int main(void) {
  float *a = createvect(NUM),
        *b = createvect(NUM);

  // test 0
  test0(NUM, a);
  setvect(NUM, a, 1);
  printf("0: a = %f\n", *a);
  
  // test 1
  test1(NUM, a, b);
  setvect(NUM, a, 1);
  setvect(NUM, b, 0);
  printf("1: a = %f, b = %f \n", *a, *b);
  
  // test 2
  test2(NUM, a);
  setvect(NUM, a, 1);
  printf("2: a = %f\n", *a);
  
  return 0;
}
