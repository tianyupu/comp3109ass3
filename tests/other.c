#include "head.h"

extern void test0(long, float *);

int main(void) {
  float *a = createvect(NUM);

  // test 0
  setvect(NUM, a, 1);
  test0(NUM, a);
  printf("0: a = %f\n", *a);
  
  return 0;
}
