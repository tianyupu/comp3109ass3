#ifndef _VECTOR
#define _VECTOR

// Assign memory for the vector
float* createvect(int length);
// Free the memory used for the vector
void delvect(float* vect);

// Assign values to every element in a vector
void setvect(int length, float* vect, float val);

// Assign values to a particular element in a vector
void assignvect(int index, float* vect, float val);

// Print a vector to stdout
void printvect(int length, float* vect);

#endif
