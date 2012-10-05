class Variable():
  def __init__(self):
    pass

  def assign(self, src, num):
    s = """
      %(src)s
      %(dest)s
      movq %%rdi, %%rbx
      movq %%rdi, %%rbx
      shrq $2, %%rbx
      jz .loop_end%(num)s
    .loop_begin%(num)s:
      movaps (%%rax), %%xmm0
      movaps %%mm0, (%%r10)
      # IMPORTANT: remove the following line only if %%rax is
      # pointing to a constant
      addq $16, %%rax
      addq $16, %%r10
      decq %%rbx
      jnz .loop_begin%(num)s
    .loop_end%(num)s:
    """ % {'src': src.load('%rax'), 'dest': self.load('%r10'), 'num': num}
    return s

class LocalVar(Variable):
  nextvar = 0
  def __init__(self):
    self.num = LocalVar.nextvar
    LocalVar.nextvar += 1

  def load(self, destreg):
    s = """
    movq %%di, %(destreg)s
    imulq $4, %(destreg)s, %(destreg)s
    addq $16, %(destreg)s
    imulq $%(num)s, %(destreg)s, %(destreg)s
    subq %%bp, %(destreg)s
    negq %(destreg)s
    andq $-16, %(destreg)s
    """ % {'num': self.num, 'destreg': destreg}
    return s

class VecParam(Variable):
  REGISTERS = ['%rsi', '%rdx', '%rcx', '%r8', '%r9']
  nextreg = 0
  def __init__(self):
    self.regno = VecParam.nextreg
    VecParam.nextreg += 1
    self.register = self.REGISTERS[self.regno]

  def load(self, destreg):
    s = 'movq %(regaddr)s, %(destreg)s' % {'regaddr': self.register, 'destreg': destreg}
    return s
