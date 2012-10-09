#include <stdlib.h>
#include <stdio.h>
#include "vector.h"

// alignment macro: aligns a memory block a to multiples of a
#define align(s,a) (((size_t)(s) + ((a)-1)) & ~ ((size_t) (a) - 1))
// alignment for SSE unit
#define SSE_ALIGN (16)


// Create a vector
float* createvect(int length) {
  return (float *) align(malloc(sizeof(float)*length + SSE_ALIGN), SSE_ALIGN);
};

// Free the memory used for the vector
void delvect(float* vect) {
  free(vect);
};

// Assign values to every element in a vector
void setvect(int length, float* vect, float val) {
  int i;
  for(i=0; i<length; i++) {
    vect[i] = val;
  }
};

// Assign values to a particular element in a vector
void assignvect(int index, float* vect, float val) {
    vect[index] = val;
};

// Print a vector to stdout
void printvect(int length, float* vect) {
  printf("<");
  int i;
  for(i=0; i<length; i++) {
    printf("%f", vect[i]);
    if (i != length-1)
      printf(", ");
  }
  printf(">");
};
