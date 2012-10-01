#!/usr/bin/python

import subprocess
import sys, os

# Configurations

# The directory containing the test programs
TEST_DIR = './tests'
# The extension for the test programs
TEST_EXT = '.vpl'

# Compilation script
COMPILE_SCRIPT = './compile.sh %s'

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


# Begin tests...
print blue('Testing VPL grammar')

# Get a list of the test programs
if ALL_TESTS:
	tests = [os.path.join(TEST_DIR, f) for f in os.listdir(TEST_DIR) if f[-4:]==TEST_EXT]
else:
	tests = [os.path.join(TEST_DIR, f+TEST_EXT) for f in TESTS]

# Get the width of the longest bash call
width = len(COMPILE_SCRIPT) + max(map(len, tests))

# Do tests
passed = 0
for test in tests:
	call = COMPILE_SCRIPT % test
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
