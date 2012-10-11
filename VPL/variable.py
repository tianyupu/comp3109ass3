class Variable():
  def __init__(self):
    pass

  def assign(self, src, loopnum):
    s = ASSIGN_ASM % {
      'src': src.load('%rax'), 'dest': self.load('%r10'), 'num': loopnum,
      'inc_source': INC_SOURCE_ASM if src.__class__.__name__ is not 'Constant' else "",
    }
    
    return s

class LocalVar(Variable):
  def __init__(self, num):
    self.num = num+1

  def load(self, destreg):
    s = VAR_LOAD_ASM % {'num': self.num, 'destreg': destreg}
    return s

class VecParam(Variable):
  REGISTERS = ['%rsi', '%rdx', '%rcx', '%r8', '%r9']
  def __init__(self, num):
    self.regno = num
    self.register = self.REGISTERS[self.regno]

  def load(self, destreg):
    s = PARAM_LOAD_ASM % {'regaddr': self.register, 'destreg': destreg}
    return s

VAR_LOAD_ASM = """
    movq %%rdi, %(destreg)s
    imulq $4, %(destreg)s, %(destreg)s
    addq $16, %(destreg)s
    imulq $%(num)s, %(destreg)s, %(destreg)s
    subq %%rbp, %(destreg)s
    negq %(destreg)s
    andq $-16, %(destreg)s
"""

PARAM_LOAD_ASM = "movq %(regaddr)s, %(destreg)s"

ASSIGN_ASM = """
    %(src)s
    %(dest)s

    movq %%rdi, %%rbx
    shrq $2, %%rbx
    jz .loop_end%(num)s
    
    .loop_begin%(num)s:
        movaps (%%rax), %%xmm0
        movaps %%xmm0, (%%r10)
        %(inc_source)s
        addq $16, %%r10
        decq %%rbx
        jnz .loop_begin%(num)s
    .loop_end%(num)s:
"""

INC_SOURCE_ASM = "addq $16, %rax"
