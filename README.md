# COMP3109 Assignment 3
============

## Resources
* [ANTLR cheat sheet](http://www.antlr.org/wiki/display/ANTLR3/ANTLR+Cheat+Sheet)
* [ANTLR python target](http://www.antlr.org/wiki/display/ANTLR3/Antlr3PythonTarget)
* [ANTLR tutorial](http://supportweb.cs.bham.ac.uk/docs/tutorials/docsystem/build/tutorials/antlr/antlr.html)

### Syntax Highlighting
For better syntax highlighting run the following command
```curl https://raw.github.com/rollxx/vim-antlr/master/syntax/antlr3.vim > ~/.vim/syntax/antlr3.vim```

Then append `au BufRead,BufNewFile *.g set syntax=antlr3` to `~/.vim/filetypes.vim` or `~/.vimrc`

## Programming

### C
To make dealing with vectors simpler there is a small collection of functions that help wil manipulating and creating vectors.
The functions are located in `vector/` and are included automatically by `compile.py`.

The following functions are included:
 * `float* createvect(int length)`  
   Create and assign memory for a vector with the given length
 * `void delvect(float* vect)`  
   Free the memory used by the given vector
 * `void setvect(int length, float* vect, float val)`  
   Set the value of each element inthe given vector
 * `void assignVect(int index, float*vect, float val)`  
   Assign the given value to the the vector at the given index.  
   Note: it is much easier to use the equivelant `vect[index] = val`.
 * `void printvect(int length, float* vect)`  
   Prints the given vector to stdout. The output is in the form `<v0, v1, ..., vn>`.

The following is an example C file that uses vectors
```C
#include <stdlib.h>
#include <stdio.h>
#include "vector.h"

// The number of elements in a vector
#define LEN 5

int main() {
  // Create vectors
  float *a = createvect(LEN),
        *b = createvect(LEN);

  // Assign values
  setvect(LEN, a, 0);
  setvect(LEN, b, 1);

  // Print vectors
  printvect(LEN, a);
  printf(", ");
  printvect(LEN, b);
  printf("\n");

  // Modify some elements
  assignvect(1, a, 1);
  assignvect(2, a, 2);
  a[3] = 3;
  a[4] = 4;
  b[0] = 3.14159;

  // Print vectors again
  printvect(LEN, a);
  printf(", ");
  printvect(LEN, b);
  printf("\n");

  return 0;
};
```
Compiling...
```shell
$./compile.py example.c
$./example
<0.000000, 0.000000, 0.000000, 0.000000, 0.000000>, <1.000000, 1.000000, 1.000000, 1.000000, 1.000000>
<0.000000, 1.000000, 2.000000, 3.000000, 4.000000>, <3.141590, 1.000000, 1.000000, 1.000000, 1.000000>
```

## Compiling
To compile use `compile.py` and the name of the file. The program will be converted to ASM and then compiled by gcc.
```shell
  $ ./compile.py prog.vpl
  $ cat prog.vpl.s
  ...<assembly file>...
  $ ./prog
  ...<program output>...
```
### Options
 * `--ANTLR=(y|n)`
  * If set to 'n' the ANTLR grammar will not be built. An already existing version will be used.
  * If set to 'y' the ANTLR grammar will be built. Even if no .vpl file is given.

### Process
 1. ANTLR builds Lexer and Parser from `VPL.g` using python
 2. The assembly (`.vpl.s`) is generated from the VPL program (`.vpl`) file using `vpl2asm.py`
   * `vpl2asm.py` uses the Lexer and Parser python library generated previously
 3. The final executable is built from a C program (`.c`) and a VPL program (`.vpl.s`) using gcc

## Tests
To perform the tests simply run `test.py` from the main folder.
```shell
  $ pwd
  .../comp3109ass3
  $ ./test.py
  Testing VPL grammar
    $ ./compile.sh ./tests/blank.vpl                      passed
    $ ./compile.sh ./tests/function.vpl                   passed
    $ ./compile.sh ./tests/multiple_functions.vpl         passed
    $ ./compile.sh ./tests/parameters.vpl                 passed
    $ ./compile.sh ./tests/declarations.vpl               passed
    $ ./compile.sh ./tests/assignment.vpl                 passed
    $ ./compile.sh ./tests/numbers.vpl                    passed
    $ ./compile.sh ./tests/operators.vpl                  passed

    Passed 8 of 8 tests
```

The `test.py` script will proceed to check that compiler
correctly identifies the programs in the test folder as syntactically valid.
If there are any errors in the compiler's output these errors will be output.

## Debugging
Debugging can be performed with `gdb <path to program>`.

(Note that `gdb` will only work effectively with programs compiled with `gcc` that have the `-g` flag.
The `compile.py` compiler does this automatically.).

### Running the program
The command `run` will run the program until the first breakpoint it comes across.
The program can be resumed after a breakpoint using this command.
The `step` command will run just one statement (ASM or C) at a time.

### Breakpoints
Breakpoints can be set at the desired positions with `break <line number>`.

### Printing values
Use `x/f $<register name>` to print out the floating point value in the register.
