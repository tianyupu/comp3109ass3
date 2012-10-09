#include "head.h"

extern void test0(long, float *);

int main(void) {
  // Create vectors
  float *a = createvect(NUM);

  // Assign values
  setvect(NUM, a, 1);

  // and invoke the function written in the vector language
  // and read values from c
  
  // test 0
  test0(NUM, a);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  return 0;
}
