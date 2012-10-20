#include "head.h"

extern void whileIf(long, float *, float *);
extern void ifWhile(long, float *, float *);
extern void moreNested(long, float *, float *, float *);
extern void stress1(long, float *, float *);

int main(void) {
  int num = 8;
  int i = 0;
  float *a = createvect(num),
        *b = createvect(num),
        *c = createvect(num);
  
  // while with an if loop inside it
  setvect(num, a, 0);
  setvect(num, b, 0);
  for (i = 0; i < num; i ++){
    a[i] = i;
    b[i] = i*i;
  }
  whileIf(num, a, b);
  printf("0: a = ");
  printvect(num, a);
  printf("\n");
  printf("   b = ");
  printvect(num, b);
  printf("\n");
 
  // such that we go into the while loop
  setvect(num, a, 0);
  setvect(num, b, 0);
  for (i = 0; i < num; i ++){
    a[i] = i-10;
    b[i] = i-5;
  }
  whileIf(num, a, b);
  printf("1: a = ");
  printvect(num, a);
  printf("\n");

  // if with a while loop inside it
  setvect(num, a, 0);
  setvect(num, b, 0);
  for (i = 0; i < num; i ++){
    a[i] = i;
    b[i] = i*i;
  }
  ifWhile(num, a, b);
  printf("2: a = ");
  printvect(num, a);
  printf("\n");
  printf("   b = ");
  printvect(num, b);
  printf("\n");

  // if with a while loop inside it
  setvect(num, a, 0);
  setvect(num, b, 0);
  for (i = 0; i < num; i ++){
    a[i] = i-10;
    b[i] = i-5;
  }
  ifWhile(num, a, b);
  printf("3: a = ");
  printvect(num, a);
  printf("\n");
  printf("   b = ");
  printvect(num, b);
  printf("\n");
  
  // more nested brackets 
  setvect(num, a, 0);
  setvect(num, b, 0);
  setvect(num, c, 0);
  for (i = 0; i < num; i ++){
    a[i] = i;
    b[i] = i*i;
    c[i] = i*2;
  }
  moreNested(num, a, b, c);
  printf("4: a = ");
  printvect(num, a);
  printf("\n");
  printf("   b = ");
  printvect(num, b);
  printf("\n");
  printf("   c = ");
  printvect(num, c);
  printf("\n");

  // stress test 1 into the first if
  num = 32;
  setvect(num, a, 0);
  setvect(num, b, 0);
  for (i = 0; i < num; i ++){
    a[i] = i;
    b[i] = i*i;
  }
  stress1(num, a, b);
  printf("5: a = ");
  printvect(num, a);
  printf("\n");
  printf("   b = ");
  printvect(num, b);
  printf("\n");

  return 0;
}
