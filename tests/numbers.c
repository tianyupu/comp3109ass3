#include "head.h"

extern void assignInt(long, float *);
extern void reassignInt(long, float *);
extern void assignFloat(long, float *);
extern void reassignFloat(long, float *);
extern void tricky(long, float *);

int main(void) {
  float *a = createvect(NUM);

  // assign an int
  setvect(NUM, a, 1);
  assignInt(NUM, a);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // assign then reassign an int
  setvect(NUM, a, 1);
  reassignInt(NUM, a);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // assign a foat
  setvect(NUM, a, 1);
  assignFloat(NUM, a);
  printf("2: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // assign then reassign a float
  setvect(NUM, a, 1);
  reassignFloat(NUM, a);
  printf("3: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // tricky example
  setvect(NUM, a, 1);
  tricky(NUM, a);
  printf("4: a = ");
  printvect(NUM, a);
  printf("\n");

  return 0;
}
