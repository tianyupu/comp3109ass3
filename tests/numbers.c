#include "head.h"

extern void test0(long, float *);
extern void test1(long, float *);
extern void test2(long, float *);
extern void test3(long, float *);
extern void test4(long, float *);

int main(void) {
  float *a = createvect(NUM);

  // test 0
  setvect(NUM, a, 1);
  test0(NUM, a);
  printf("0: a = %f \n", *a);
  
  // test 1
  setvect(NUM, a, 1);
  test1(NUM, a);
  printf("1: a = %f \n", *a);
  
  // test 2
  setvect(NUM, a, 1);
  test2(NUM, a);
  printf("2: a = %f \n", *a);
  
  // test 3
  setvect(NUM, a, 1);
  test3(NUM, a);
  printf("3: a = %f \n", *a);
  
  // test 4
  setvect(NUM, a, 1);
  test4(NUM, a);
  printf("4: a = %f \n", *a);

  return 0;
}
