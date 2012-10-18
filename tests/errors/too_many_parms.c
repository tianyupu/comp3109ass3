#include "head.h"

extern void sixPar(long, float *, float *, float *, float *, float *, float *);

int main(void) {
  // Create vectors
  float *a = createvect(NUM),
        *b = createvect(NUM),
        *c = createvect(NUM),
        *d = createvect(NUM),
        *e = createvect(NUM),
        *f = createvect(NUM);

  // Assign dummy values
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  setvect(NUM, c, 3);
  setvect(NUM, d, 4);
  setvect(NUM, e, 5);
  setvect(NUM, f, 6);
  
  // 6 parameters
  // this is more than the maximum amount of parameters we can have
  // this should break
  sixPar(NUM, a, b, c, d, e, f);
  printf("0: a = ");
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
  printf("   f = ");
  printvect(NUM, f);
  printf("\n");
  
  return 0;
}
