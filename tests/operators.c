#include "head.h"

extern void test0(long, float *);
extern void test1(long, float *, float *);
extern void test2(long, float *);

int main(void) {
  float *a = createvect(NUM),
        *b = createvect(NUM);

  // test 0
  setvect(NUM, a, 1);
  test0(NUM, a);

  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // test 1
  setvect(NUM, a, 1);
  setvect(NUM, b, 0);
  test1(NUM, a, b);

  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // test 2
  setvect(NUM, a, 1);
  test2(NUM, a);

  printf("2: a = ");
  printvect(NUM, a);
  printf("\n");
  
  return 0;
}
