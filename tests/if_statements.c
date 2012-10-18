#include "head.h"

extern void basic(long, float *);
extern void redundant(long, float *);
extern void nested(long, float *, float *);
extern void twoIf(long, float *, float *);
extern void empty(long, float *, float *);

int main(void) {
  float *a = createvect(NUM),
        *b = createvect(NUM);

  // basic if
  setvect(NUM, a, 1);
  basic(NUM, a);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // redundant if test (executes for no reason) 
  setvect(NUM, a, 1);
  redundant(NUM, a);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // a nested if loop where a should be 5, b should be 10 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  nested(NUM, a, b);
  printf("2: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // a nested if loop where a should be 3, and b is unchanged 
  setvect(NUM, a, 1);
  setvect(NUM, b, 20.5);
  nested(NUM, a, b);
  printf("3: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // two consequitive if statements 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  twoIf(NUM, a, b);
  printf("4: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // empty if statement 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  empty(NUM, a, b);
  printf("5: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  return 0;
}
