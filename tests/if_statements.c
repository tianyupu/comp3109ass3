#include "head.h"

extern void basic(long, float *);
extern void redundant(long, float *);
extern void compare(long, float *, float *);
extern void nested(long, float *, float *);
extern void equal(long, float *, float *);
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
  
  // compares a & b
  // a is 5 if less than b, else 0
  // here a is less than b (so 5)
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  compare(NUM, a, b);
  printf("2: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");

  // compares a & b
  // here a should be 0
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  compare(NUM, a, b);
  printf("3: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // a nested if loop where a should be 7 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  nested(NUM, a, b);
  printf("4: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // a nested if loop where a should be 3 
  setvect(NUM, a, 1);
  setvect(NUM, b, 20.5);
  nested(NUM, a, b);
  printf("5: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // tests a < b where a == b 
  setvect(NUM, a, 2);
  setvect(NUM, b, 1);
  equal(NUM, a, b);
  printf("6: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // two consequitive if statements 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  equal(NUM, a, b);
  printf("7: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // empty if statement 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  equal(NUM, a, b);
  printf("8: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  return 0;
}
