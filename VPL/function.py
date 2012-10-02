class Function():
  def __init__(self, name, params):
    self.name = name
    self.params = params

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
    """ % {'name': name, 'num': len(self.params)}   
    
    self.after = """
    # epilog of a function
    popq %rbx # restore reg %rbx
    leave # restore frame pointer
    ret # return"""

    # TO DO
    self.body = """
    """

  def __str__(self):
    return self.before + self.body + self.after
