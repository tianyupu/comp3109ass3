#include "head.h"

extern void bracket(long, float *);
extern void bracketedOperations(long, float *, float *);
extern void mins(long, float *, float *);
extern void trickyOrderOperations(long, float *, float *);
extern void nested(long, float *, float *);
extern void moreNested(long, float *, float *, float *);

int main(void) {
  float *a = createvect(NUM),
        *b = createvect(NUM),
        *c = createvect(NUM);

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
  
  // tricky order of operations 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  trickyOrderOperations(NUM, a, b);
  printf("3: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // nested brackets 
  setvect(NUM, a, 1);
  setvect(NUM, b, 3);
  nested(NUM, a, b);
  printf("4: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  
  // more nested brackets 
  setvect(NUM, a, 2);
  setvect(NUM, b, 3);
  setvect(NUM, c, 4);
  moreNested(NUM, a, b, c);
  printf("5: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  printf("   c = ");
  printvect(NUM, c);
  printf("\n");

  return 0;
}
