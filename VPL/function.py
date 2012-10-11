from constant import Constant
from variable import *
from expression import Expression

class Function():
  def __init__(self, ast_node, prog):
    # Reference to the program
    self.prog = prog

    # Get the function properties
    name, params, localvars, statements = ast_node.children

    # The name of the function
    self.name = name.text

    # Dictionaries for variables, parameters and statements
    self.params = {p.text: VecParam(i)
        for i, p in enumerate(params.children)}
    
    self.localvars = {v.text: LocalVar(i)
        for i, v in enumerate(localvars.children)}

    self.statements = statements

    # Run statements
    self.body = ""
    for statement in self.statements.children:
      # Assignment
      if statement.token.text == "ASSIGN":
        # Get the variable and expression
        var, expr = statement.children
        var = self.getVar(var.text)

        # Calculate the answer
        expr = Expression(expr, self)
        factor = expr.evaluate()
        
        # Add the calculations to the function body
        self.body += expr.asm
        self.body += var.assign(factor, self.prog.next_loop)
        self.prog.next_loop += 1

    self.before = FUNC_START_ASM
    self.after = FUNC_END_ASM

  def getVar(self, ident):
    if ident in self.params:
      return self.params[ident]
    if ident in self.localvars:
      return self.localvars[ident]

    return self.prog.addConst(float(ident))

  def tempVar(self):
    # Get a number for the variable
    num = len(self.localvars)
    # Add new local variable
    var = self.localvars['temp'+str(num)] = LocalVar(num)
    return var

  def __str__(self):
    before = self.before % {'name': self.name, 'num': len(self.localvars)}
    return before + self.body + self.after

FUNC_START_ASM = """
.text
.global %(name)s
.type %(name)s, @function
.p2align 4,,15

%(name)s:
    pushq %%rbp                       # save current frame pointer on stack
    movq %%rsp, %%rbp                 # set frame pointer
    pushq %%rbx                       # save callee-save registers that are used on stack

    # Allocating memory for local variables
    # Allocate %(num)s local variable(s)
    movq %%rdi, %%rax
    imulq $4, %%rax, %%rax
    addq $16, %%rax
    imulq $%(num)s, %%rax, %%rax
    subq %%rax, %%rsp
    andq $-16, %%rsp
"""

FUNC_END_ASM = """
    # Epilog of a function
    popq %rbx                         # restore reg %rbx
    leave                             # restore frame pointer
    ret                               # return
"""
