#include "head.h"

extern void endless(long, float *);

int main(void) {
  float *a = createvect(NUM);
  setvect(NUM, a, 1);

  // endless loop 
  endless(NUM, a);
  printf("0: a = ");
  printvect(NUM, a);
  printf("\n");
  
  return 0;
}
