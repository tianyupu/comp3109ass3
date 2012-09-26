#!/bin/bash
set -e

BUILD_DIR=build

if [ ${#} != 1 ]; then
  echo "Usage: ${0} filename.vpl" >&2
  exit 1
fi

# builds the ANTLR-generated parser using the grammar file
java -cp antlr-3.1.2.jar org.antlr.Tool -o ${BUILD_DIR} VPL.g
touch ${BUILD_DIR}/__init__.py

# uses the ANTLR-generated parser to convert the VPL program to ASM
./vpl2asm.py < ${1} > ${1}.s

# compiles the ASM and C file together
gcc -Wall -W main.c ${1}.s -o my_program
