#include "head.h"

extern void bracket(long, float *);
extern void bracketedOperations(long, float *, float *);
extern void mins(long, float *, float *);
extern void trickyOrderOperations(long, float *, float *);

int main(void) {
  float *a = createvect(NUM),
        *b = createvect(NUM);

  // simple brackets 
  setvect(NUM, a, 1);
  bracket(NUM, a);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  // Operations which are in bracket or left to write order already 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  bracketedOperations(NUM, a, b);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // minimums 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  mins(NUM, a, b);
  printf("2: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // ricky order of operations 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  trickyOrderOperations(NUM, a, b);
  printf("3: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  return 0;
}
