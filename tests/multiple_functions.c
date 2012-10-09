#include "head.h"

extern void test0(long, float *);
extern void test1(long, float *);

int main(void) {
  // Create vectors
  float *a = createvect(NUM);

  // Assign values
  setvect(NUM, a, 1);
  
  // test 0
  test0(NUM, a);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // test 1
  test1(NUM, a);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  
  return 0;
}
