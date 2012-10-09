from constant import Constant
from variable import *

class Function():
  def __init__(self, name, params, localvars):
    self.name = name

    # Dictionaries for variables, parameters and constants
    self.params = params if params else {}
    self.localvars = localvars if localvars else {}
    self.consts = {}

    self.before = """
    .text
    .global %(name)s
    .type %(name)s, @function
    .p2align 4,,15
    
    %(name)s:
      # save current frame pointer on stack
      pushq %%rbp
      # set frame pointer
      movq %%rsp, %%rbp
      # save callee-save registers that are used on stack
      pushq %%rbx

    # Allocating memory for local variables
    # Allocate NUM local Variable
    movq %%rdi, %%rax
    imulq $4, %%rax, %%rax
    addq $16, %%rax
    # NUM is the number of local variables
    # Needs to be computed by an attribute in the attribute grammar
    imulq $%(num)s, %%rax, %%rax
    subq %%rax, %%rsp
    andq $-16, %%rsp
    """    
    
    self.after = """
    # epilog of a function
    popq %rbx # restore reg %rbx
    leave # restore frame pointer
    ret # return"""

    # TO DO
    self.body = """
    """
  def getVar(self, ident):
    if ident in self.params:
      return self.params[ident]
    elif ident in self.localvars:
      return self.localvars[ident]

  def __str__(self):
    return self.before % {'name': self.name, 'num': len(self.localvars)} \
        + self.body \
        + '\n'.join(map(str, self.consts.values())) \
        + self.after
