#!/usr/bin/python
import sys, os

BUILD_DIR = 'build'

usage = "Usage: %s filename.[vpl|c] [--ANTLR=(y|n)]" % sys.argv[0]

# Check to see if given a program to compile
if len(sys.argv) < 2:
  print usage
  sys.exit(1)
else:
  if '.vpl' in sys.argv[1]:
    prog = sys.argv[1].rstrip('.vpl')
    ext = "vpl"
  elif '.c' in sys.argv[1]:
    prog = sys.argv[1].rstrip('.c')
    ext = "c"
  elif "--ANTLR" in sys.argv[1]:
    prog = None
    ext = None
  else:
    print usage
    sys.exit(1)

# Build the ANTLR-generated parser using the grammar file
if '--ANTLR=n' not in sys.argv or "--ANTLR=y" in sys.argv and ext!="c":
  os.system("java -cp antlr-3.1.2.jar org.antlr.Tool -o %s VPL.g" % BUILD_DIR)
  os.system("touch %s" % os.path.join(BUILD_DIR, '__init__.py'))

# Use the ANTLR-generated parser to convert the VPL program to ASM
if prog:
  if ext == "vpl":
    os.system("./vpl2asm.py < %(prog)s.vpl > %(prog)s.vpl.s" % {'prog': prog})
  
  # Compile options
  call = "gcc -g -Wall -W -I vector vector/vector.c -o %(prog)s "

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

