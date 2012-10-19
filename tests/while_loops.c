#include "head.h"

extern void basicIncrement(long, float *);
extern void nested(long, float *, float *);
extern void nested2(long, float *, float *);
extern void relativeChange(long, float *, float *);
extern void whileIf(long, float *, float *);

int main(void) {
  float *a = createvect(NUM),
        *b = createvect(NUM);
  
  // incrementing up to 20 
  setvect(NUM, a, 1);
  basicIncrement(NUM, a);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // nested while loop
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  nested(NUM, a, b);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // nested while loop
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  nested2(NUM, a, b);
  printf("2: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // a and b changing relative to each other
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  relativeChange(NUM, a, b);
  printf("3: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // while with an if loop inside it
  setvect(NUM, a, 1);
  setvect(NUM, b, 3);
  whileIf(NUM, a, b);
  printf("4: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");

  return 0;
}
