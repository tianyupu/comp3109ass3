#include "head.h"

extern void test0(long, float *, float *);
extern void test1(long, float *, float *);
extern void test2(long, float *, float *, float *);

int main(void) {
  float *a = createvect(NUM),
        *b = createvect(NUM),
        *c = createvect(NUM);

  // test 0
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  test0(NUM, a, b);
  printf("0: a = %f, b = %f \n", *a, *b);
  
  // test 1
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  test1(NUM, a, b);
  printf("1: a = %f, b = %f \n", *a, *b);
  
  // test 2
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  setvect(NUM, c, 3);
  test2(NUM, a, b, c);
  printf("2: a = %f, b = %f, c = %f \n", *a, *b, *c);
  
  return 0;
}
