#!/usr/bin/python
import sys, os

BUILD_DIR = 'build'

usage = "Usage: %s filename.[vpl|c] [--ANTLR=(y|n)]" % sys.argv[0]

# Check to see if given a program to compile
if len(sys.argv) < 2:
  print usage
  sys.exit(1)
else:
  prog, ext = None, None
  antlr = None

  for arg in sys.argv[1:]:
    if "--ANTLR" in arg:
      antlr = arg[-1]

    if not os.path.isfile(arg):
      continue

    prog, ext = os.path.splitext(arg)
    if ext == '.vpl':
      ext = "vpl"
    elif ext == '.c':
      ext = "c"
    else:
      ext = None

if ext == None and antlr == None:
  print usage
  sys.exit(1)

# Build the ANTLR-generated parser using the grammar file
if antlr == "n" or (antlr == "y" and ext!="c"):
  os.system("java -cp antlr-3.1.2.jar org.antlr.Tool -o %s VPL.g" % BUILD_DIR)
  os.system("touch %s" % os.path.join(BUILD_DIR, '__init__.py'))

# Use the ANTLR-generated parser to convert the VPL program to ASM
if prog:
  if ext == "vpl":
    os.system("./vpl2asm.py < %(prog)s.vpl > %(prog)s.vpl.s" % {'prog': prog})
  
  # Compile options
  call = "gcc -g -Wall -W -Ivector -Itests vector/vector.c -o %(prog)s "

  # Choose C file
  if os.path.isfile(prog+'.c'):
    # Use prog.c
    call += "%(prog)s.c "
  else:
    # Use main.c
    call += "main.c "

  # Include assembly
  if os.path.isfile(prog+'.vpl.s'):
    call += "%(prog)s.vpl.s"

  # Compile
  os.system(call % {'prog': prog})

