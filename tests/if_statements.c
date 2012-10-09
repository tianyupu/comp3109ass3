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
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // test 1
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  test1(NUM, a, b);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // test 2
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  setvect(NUM, c, 3);
  test2(NUM, a, b, c);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  printf("   c = ");
  printvect(NUM, c);
  printf("\n");
  
  return 0;
}
