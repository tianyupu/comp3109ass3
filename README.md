# COMP3109 Assignment 3
============

## Resources
* [ANTLR cheat sheet](http://www.antlr.org/wiki/display/ANTLR3/ANTLR+Cheat+Sheet)
* [ANTLR python target](http://www.antlr.org/wiki/display/ANTLR3/Antlr3PythonTarget)
* [ANTLR tutorial](http://supportweb.cs.bham.ac.uk/docs/tutorials/docsystem/build/tutorials/antlr/antlr.html)

### Syntax Highlighting
For better syntax highlighting run the following command
```curl https://raw.github.com/rollxx/vim-antlr/master/syntax/antlr3.vim > ~/.vim/syntax/antlr3.vim```

Then append `au BufRead,BufNewFile *.g set syntax=antlr3` to `~/.vim/filetypes.vim`


## Compiling
To compile use `compile.py` and the name of the file. The program will be converted to ASM and then compiled by gcc.
```shell
  $ ./compile.py prog.vpl
  $ cat prog.vpl.s
  ...
  $ ./prog.vpl
  ...
```
### Options
 * `--ANTLR=(y|n)`
  * If set to 'n' the ANTLR grammar will not be built. An already existing version will be used.
  * If set to 'y' the ANTLR grammar will be built. Even if no .vpl file is given.


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