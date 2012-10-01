#!/usr/bin/python

import subprocess
import sys, os

TEST_DIR = './tests'


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
tests = [os.path.join(TEST_DIR, f) for f in os.listdir(TEST_DIR) if f[-4:]=='.vpl']
# Compilation script
script = './compile.sh %s'

# Do tests
passed = 0
for test in tests:
	call = script % test
	print ('  $ %s' % call).ljust(50)
	
	result = os.popen("bash -c '%s'" % call).read()
	
	if not result:
		print green("passed")
		passed += 1
	else:
		print red("failed")
		print red(result)
print

result = "  Passed %d of %d tests" % (passed, len(tests))
if passed == len(tests):
	print green(result)
else:
	print red(result)

print
