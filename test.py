#!/usr/bin/python

import subprocess
import sys, os

# Configurations

# The directory containing the test programs
TEST_DIR = './tests'
# The extension for the test programs
PROG_EXT = '.vpl'
# The extension for checking the output of compile programs
TEST_EXT = '.ans'

# Compilation script
COMPILE_SCRIPT = './compile.py %(test)s'+PROG_EXT+' --ANTLR=n'
# Script for checking output of compiled program
OUTPUT_TEST_SCRIPT = 'diff %(test)s %(test)s'+TEST_EXT

# Set to true to true for all tests
# Set to false for specified subset
ALL_TESTS = False
# Subset of tests
TESTS = [
	'blank',
	'function',
	'multiple_functions',
	'parameters',
	'declarations',
	'assignment',
	'numbers',
	'operators',
	'expressions',
	'if_statements',
	'while_loops',
	'other',
]


# Output to shell
class echo():
	def write(self, string):
		string = string.replace('"', '\\"')
		subprocess.call('echo -ne "%s"' % string, shell=True)

sys.stdout = echo()


# Colour output
def blue(string):
	return "\e[1;34m"+string+"\e[0m"

def red(string):
	return "\e[1;31m"+string+"\e[0m"

def green(string):
	return "\e[1;32m"+string+"\e[0m"

# Test function
def run_tests(command, tests, name="Test"):
  # Print the name of the tests
  print blue('\t'+name)
  
  # Get the width of the longest command
  width = len(command) + max(map(len, tests))
  
  # Do the tests
  passed = 0
  for test in tests:
    call = command % {'test': test}
    print ('  $ %s' % call).ljust(width+10),
    
    # Run compilation and read for errors
    stdin, stdout, stderr = os.popen3(call)
    stderr = stderr.read()
    
    # Check results
    if not stderr:
      print green("passed")
      passed += 1
    else:
      print red("failed")
      print red(stderr)
    
  print

  # Overall test results
  result = "  Passed %d of %d tests" % (passed, len(tests))
  if passed == len(tests):
    print green(result)
  else:
    print red(result)
  
  print

# Begin tests...
print blue('Testing VPL grammar')

# Get a list of the test programs
if ALL_TESTS:
  tests = [os.path.join(TEST_DIR, f[:-4]) for f in os.listdir(TEST_DIR) if f[-4:]==PROG_EXT]
else:
	tests = [os.path.join(TEST_DIR, f) for f in TESTS]


# Compilation tests
os.system("./compile.py --ANTLR=y")
run_tests(COMPILE_SCRIPT, tests, "Compilation tests")

# Output tests
run_tests(OUTPUT_TEST_SCRIPT, tests, "Output tests")

