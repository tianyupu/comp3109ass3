#include "head.h"

extern void test0(long, float *);
extern void test1(long, float *, float *);
extern void test2(long, float *, float *);
extern void test3(long, float *, float *);

int main(void) {
  float *a = createvect(NUM),
        *b = createvect(NUM);

  // setting the vectors
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);

  // test 0
  test0(NUM, a);
  printf("0: a = %f\n", *a);
  
  // test 1
  setvect(NUM, a, 1);
  test1(NUM, a, b);
  printf("1: a = %f, b = %f\n", *a, *b);
  
  // test 2
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  test2(NUM, a, b);
  printf("2: a = %f, b = %f\n", *a, *b);
  
  // test 3
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  test3(NUM, a, b);
  printf("3: a = %f, b = %f\n", *a, *b);

  return 0;
}
