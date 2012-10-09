#include "head.h"

extern void test0(long, float *);
extern void test1(long, float *);

int main(void) {
  float *a = createvect(NUM);
  setvect(NUM, a, 1);

  // test 0
  test0(NUM, a);
  printf("0: %f\n", *a);
  
  // test 1
  test1(NUM, a);
  printf("1: %f\n", *a);
  
  return 0;
}
