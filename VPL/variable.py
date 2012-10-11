class Variable():
  def __init__(self):
    pass

  def assign(self, src, loopnum):
    s = ASSIGN_ASM.format(
      src = src.load('%rax'), dest = self.load('%r10'), loop = loopnum,
      inc_source = INC_SOURCE_ASM if src.__class__.__name__ is not 'Constant' else "",
    )
    
    return s

class LocalVar(Variable):
  def __init__(self, num):
    self.num = num+1

  def load(self, destreg):
    s = VAR_LOAD_ASM.format(num=self.num, destreg=destreg)
    return s

class VecParam(Variable):
  REGISTERS = ['%rsi', '%rdx', '%rcx', '%r8', '%r9']
  def __init__(self, num):
    self.regno = num
    self.register = self.REGISTERS[self.regno]

  def load(self, destreg):
    s = PARAM_LOAD_ASM.format(regaddr=self.register, destreg=destreg)
    return s

VAR_LOAD_ASM = """movq %rdi, {destreg}
    imulq $4, {destreg}, {destreg}
    addq $16, {destreg}
    imulq ${num}, {destreg}, {destreg}
    subq %rbp, {destreg}
    negq {destreg}
    andq $-16, {destreg}"""

PARAM_LOAD_ASM = "movq {regaddr}, {destreg}"

ASSIGN_ASM = """
    {src}
    {dest}

    movq %rdi, %rbx
    shrq $2, %rbx
    jz .loop_end{loop}
    
    .loop_begin{loop}:
        movaps (%rax), %xmm0
        movaps %xmm0, (%r10)
        {inc_source}
        addq $16, %r10
        decq %rbx
        jnz .loop_begin{loop}
    .loop_end{loop}:
"""

INC_SOURCE_ASM = "addq $16, %rax"
