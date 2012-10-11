#!/usr/bin/env python
import sys
import antlr3
from build.VPLLexer import VPLLexer
from build.VPLParser import VPLParser

import VPL

char_stream = antlr3.ANTLRInputStream(sys.stdin)
lexer = VPLLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = VPLParser(tokens)
root = parser.program()

program = VPL.Program(root.tree)
print program
