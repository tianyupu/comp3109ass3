#include "head.h"

extern void foobar(long, float *, float *, float *);
extern void foobaz(long, float *, float *, float *);

int main(void) {
  int num = 16;
  float *a = createvect(num),
        *b = createvect(num),
        *c = createvect(num);
  
  setvect(NUM, a, 1);
  setvect(NUM, b, 1);
  setvect(NUM, c, 1);
  int i;
  for (i = 0; i != num; i++) {
    a[i] = i;
    b[i] = num - i - 1;
  }
 
  // given addition test
  foobar(NUM, a, b, c);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  printf("   b = ");
  printvect(NUM, b);
  printf("\n");
  printf("   c = ");
  printvect(NUM, c);
  printf("\n");
  
  setvect(NUM, a, 1);
  setvect(NUM, b, 1);
  setvect(NUM, c, 1);
  for (i = 0; i != num; i++) {
    a[i] = i;
    b[i] = num - i - 1;
  }
  
  // given addition test
  foobaz(NUM, a, b, c);
  printf("1: a = ");
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
