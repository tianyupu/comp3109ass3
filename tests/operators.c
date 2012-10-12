#include "head.h"

extern void numAddition(long, float *);
extern void parAddition(long, float *, float *);
extern void allOperators(long, float *, float *);

int main(void) {
  float *a = createvect(NUM),
        *b = createvect(NUM);

  // addition of constants
  setvect(NUM, a, 1);
  numAddition(NUM, a);

  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // addition involving the parameters 
  setvect(NUM, a, 1);
  setvect(NUM, b, 0);
  parAddition(NUM, a, b);

  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // all possible operations
  setvect(NUM, a, 1);
  setvect(NUM, b, 0);
  allOperators(NUM, a, b);

  printf("2: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  return 0;
}
