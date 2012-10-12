#include "head.h"

extern void basic(long, float *);
extern void twoVar(long, float *, float *);
extern void tricky(long, float *, float *);
extern void aToB(long, float *, float *);
extern void swapVar(long, float *, float *);

int main(void) {
  float *a = createvect(NUM),
        *b = createvect(NUM);

  // setting the vectors
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);

  // basic 
  basic(NUM, a);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // two variables
  setvect(NUM, a, 1);
  twoVar(NUM, a, b);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // tricky example
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  tricky(NUM, a, b);
  printf("2: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // assigning A to b
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  aToB(NUM, a, b);
  printf("3: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");

  // swaping A and B
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  swapVar(NUM, a, b);
  printf("4: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  return 0;
}
