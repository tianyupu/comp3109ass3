#include "head.h"

extern void test0(long, float *);
extern void test1(long, float *, float *);
extern void test2(long, float *, float *, float *, float *);

int main(void) {
  // Create vectors
  float *a = createvect(NUM),
        *b = createvect(NUM),
        *c = createvect(NUM),
        *d = createvect(NUM);

  // Assign dummy values
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  setvect(NUM, c, 3);
  setvect(NUM, d, 4);

  // test 0
  test0(NUM, a);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // test 1
  test1(NUM, a, b);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // test 2
  test2(NUM, a, b, c, d);
  printf("2: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  printf("   c = ");
  printvect(NUM, c);
  printf("\n");
  printf("   d = ");
  printvect(NUM, d);
  printf("\n");
  
  return 0;
}
