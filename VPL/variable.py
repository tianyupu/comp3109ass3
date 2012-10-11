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
  def __init__(self, name, num):
    self.name = name
    self.num = num+1

  def load(self, destreg):
    s = VAR_LOAD_ASM.format(name=self.name, num=self.num, destreg=destreg)
    return s

class VecParam(Variable):
  REGISTERS = ['%rsi', '%rdx', '%rcx', '%r8', '%r9']
  def __init__(self, name, num):
    self.name = name
    self.regno = num
    self.register = self.REGISTERS[self.regno]

  def load(self, destreg):
    s = PARAM_LOAD_ASM.format(name=self.name, regaddr=self.register, destreg=destreg)
    return s

VAR_LOAD_ASM = """movq %rdi, {destreg:<23} # load local variable #{num},
    imulq $4, {destreg:<4}, {destreg:<18} # '{name}' into {destreg}
    addq $16, {destreg:<24} # 
    imulq ${num:<4}, {destreg:<4}, {destreg:<15} #
    subq %rbp, {destreg:<23} #
    negq {destreg:<29} #
    andq $-16, {destreg:<23} # """

PARAM_LOAD_ASM = "movq {regaddr:<4}, {destreg:<23} # load parameter '{name}' into {destreg}"

ASSIGN_ASM = """
    # load source
    {src}
    # load destination
    {dest}

    movq %rdi, %rbx                    # load vector length into counter %rbx
    shrq $2, %rbx                      # divide counter reg by 4
                                       # (per loop iteration 4 floats)
    jz .loop_end{loop:<22} # check whether number is equal to zero
    
    .loop_begin{loop}:
        movaps (%rax), %xmm0           # load source into %xmm0
        movaps %xmm0, (%r10)           # load %xmm0 into destination

        {inc_source:<30} # increment source counter
        addq $16, %r10                 # increment destination counter
        
        decq %rbx                      # decrement loop counter
        jnz .loop_begin{loop:<15} # jump to loop header if counter is not zero
    .loop_end{loop}:
"""

INC_SOURCE_ASM = "addq $16, %rax"
