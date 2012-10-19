#include "head.h"

extern void whileIf(long, float *, float *);
extern void ifWhile(long, float *, float *);
extern void moreNested(long, float *, float *);
extern void stress1(long, float *, float *);

int main(void) {
  NUM = 8;
  float *a = createvect(NUM),
        *b = createvect(NUM),
        *c = createvect(NUM);
  
  // while with an if loop inside it
  setvect(NUM, a, 0);
  a[1] = 1;
  a[2] = 2;
  a[3] = 3;
  a[4] = 4;
  a[5] = 5;
  setvect(NUM, b, 3);
  b[0] = 0;
  b[5] = 10;
  whileIf(NUM, a, b);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");

  // if with a while loop inside it
  setvect(NUM, a, 1);
  a[1] = 1;
  a[2] = 2;
  a[3] = 3;
  a[4] = 4;
  a[5] = 5;
  setvect(NUM, b, 0);
  b[0] = 0;
  b[5] = 10;
  ifWhile(NUM, a, b);
  printf("1: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");

  // more nested brackets 
  setvect(NUM, a, 2);
  a[1] = 1;
  a[2] = 2;
  a[3] = 3;
  a[4] = 4;
  a[5] = 5;
  setvect(NUM, b, 0);
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

  // stress test 1 into the first if 
  setvect(NUM, a, 1);
  setvect(NUM, b, 2);
  stress1(32, a, b);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");

  return 0;
}
