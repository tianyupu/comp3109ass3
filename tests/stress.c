#include "head.h"

extern void stress1(long, float *, float *);
extern void stress2(long, float *, float *);
extern void stress3(long, float *, float *, float *, float *, float *);

int main(void) {
  // Create vectors
  float *a = createvect(NUM),
        *b = createvect(NUM),
        *c = createvect(NUM),
        *d = createvect(NUM),
        *e = createvect(NUM);

  // Assign dummy values
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  setvect(NUM, c, 3);
  setvect(NUM, d, 4);
  setvect(NUM, e, 5);

  // stress test 1 into the first if 
  stress1(NUM, a, b);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // stress test 1 into the else of the first if 
  setvect(NUM, a, 100);
  setvect(NUM, b, 200);
  stress1(NUM, a, b);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  
  // stress test 2 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  stress2(NUM, a, b);
  printf("2: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // stress test 3 
  stress3(NUM, a, b, c, d, e);
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  printf("3: a = ");
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
  printf("   e = ");
  printvect(NUM, e);
  printf("\n");
  
  return 0;
}
