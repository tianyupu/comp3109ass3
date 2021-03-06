#include "head.h"

extern void onePar(long, float *);
extern void twoPar(long, float *, float *);
extern void fivePar(long, float *, float *, float *, float *, float *);

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

  // 1 parameter
  onePar(NUM, a);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // 2 parameter
  twoPar(NUM, a, b);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // 5 parameters
  // this is the maximum amount of parameters we can have
  fivePar(NUM, a, b, c, d, e);
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
  printf("   e = ");
  printvect(NUM, e);
  printf("\n");
  
  return 0;
}
